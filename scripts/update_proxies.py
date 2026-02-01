#!/usr/bin/env python3
"""
从openproxylist.com抓取V2Ray节点并生成Karing订阅文件
支持base64编码和纯文本格式
"""

import requests
import base64
import json
from datetime import datetime
import os

# openproxylist GitHub仓库的raw文件链接
V2RAY_SOURCE = "https://raw.githubusercontent.com/roosterkid/openproxylist/main/V2RAY_BASE64.txt"
V2RAY_RAW_SOURCE = "https://raw.githubusercontent.com/roosterkid/openproxylist/main/V2RAY.txt"

def fetch_proxies():
    """从openproxylist获取V2Ray节点"""
    print(f"[{datetime.now()}] 开始获取节点列表...")
    
    try:
        # 获取base64编码的节点
        response = requests.get(V2RAY_SOURCE, timeout=30)
        response.raise_for_status()
        base64_content = response.text.strip()
        
        # 获取原始格式节点
        response_raw = requests.get(V2RAY_RAW_SOURCE, timeout=30)
        response_raw.raise_for_status()
        raw_content = response_raw.text.strip()
        
        # 解码base64获取节点列表
        decoded = base64.b64decode(base64_content).decode('utf-8')
        proxy_list = [line.strip() for line in decoded.split('\n') if line.strip()]
        
        print(f"成功获取 {len(proxy_list)} 个节点")
        return proxy_list, raw_content, base64_content
        
    except Exception as e:
        print(f"获取节点失败: {e}")
        return [], "", ""

def generate_clash_subscription(proxies):
    """生成Clash格式订阅"""
    clash_config = {
        "port": 7890,
        "socks-port": 7891,
        "allow-lan": False,
        "mode": "rule",
        "log-level": "info",
        "external-controller": "127.0.0.1:9090",
        "proxies": [],
        "proxy-groups": [
            {
                "name": "PROXY",
                "type": "select",
                "proxies": ["自动选择"] + []
            },
            {
                "name": "自动选择",
                "type": "url-test",
                "proxies": [],
                "url": "http://www.gstatic.com/generate_204",
                "interval": 300
            }
        ],
        "rules": [
            "MATCH,PROXY"
        ]
    }
    
    # 解析V2Ray链接并添加到配置
    for idx, proxy in enumerate(proxies):
        if proxy.startswith("vmess://"):
            try:
                # 解码vmess链接
                vmess_data = json.loads(base64.b64decode(proxy[8:]).decode('utf-8'))
                proxy_item = {
                    "name": vmess_data.get("ps", f"节点-{idx+1}"),
                    "type": "vmess",
                    "server": vmess_data.get("add", ""),
                    "port": int(vmess_data.get("port", 443)),
                    "uuid": vmess_data.get("id", ""),
                    "alterId": int(vmess_data.get("aid", 0)),
                    "cipher": "auto",
                    "network": vmess_data.get("net", "tcp")
                }
                
                # 添加TLS配置
                if vmess_data.get("tls") == "tls":
                    proxy_item["tls"] = True
                    if vmess_data.get("sni"):
                        proxy_item["servername"] = vmess_data.get("sni")
                
                # 添加WebSocket配置
                if proxy_item["network"] == "ws":
                    proxy_item["ws-opts"] = {
                        "path": vmess_data.get("path", "/"),
                        "headers": {}
                    }
                    if vmess_data.get("host"):
                        proxy_item["ws-opts"]["headers"]["Host"] = vmess_data.get("host")
                
                clash_config["proxies"].append(proxy_item)
                clash_config["proxy-groups"][0]["proxies"].append(proxy_item["name"])
                clash_config["proxy-groups"][1]["proxies"].append(proxy_item["name"])
                
            except Exception as e:
                print(f"解析节点失败: {e}")
                continue
    
    return clash_config

def save_subscriptions(proxies, raw_content, base64_content):
    """保存多种格式的订阅文件"""
    os.makedirs("subscriptions", exist_ok=True)
    
    # 1. Base64编码的订阅 (V2Ray标准格式)
    with open("subscriptions/v2ray_base64.txt", "w", encoding="utf-8") as f:
        f.write(base64_content)
    print("✓ 保存 V2Ray Base64 订阅")
    
    # 2. 纯文本订阅 (每行一个节点链接)
    with open("subscriptions/v2ray.txt", "w", encoding="utf-8") as f:
        f.write(raw_content)
    print("✓ 保存 V2Ray 纯文本订阅")
    
    # 3. Clash订阅
    try:
        clash_config = generate_clash_subscription(proxies)
        import yaml
        with open("subscriptions/clash.yaml", "w", encoding="utf-8") as f:
            yaml.dump(clash_config, f, allow_unicode=True, default_flow_style=False)
        print("✓ 保存 Clash 订阅")
    except Exception as e:
        print(f"生成Clash订阅失败: {e}")
    
    # 4. 生成统计信息
    stats = {
        "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_proxies": len(proxies),
        "source": "openproxylist.com"
    }
    
    with open("subscriptions/stats.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    print("✓ 保存统计信息")
    
    # 5. 生成README
    readme_content = f"""# 代理订阅服务

> 自动从 [openproxylist.com](https://openproxylist.com) 抓取免费V2Ray节点

## 📊 订阅信息

- **更新时间**: {stats['update_time']}
- **节点数量**: {stats['total_proxies']}
- **数据来源**: openproxylist.com
- **更新频率**: 每2小时自动更新

## 🔗 订阅链接

### V2Ray Base64订阅 (推荐)
```
https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/subscriptions/v2ray_base64.txt
```

### V2Ray 纯文本订阅
```
https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/subscriptions/v2ray.txt
```

### Clash订阅
```
https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/subscriptions/clash.yaml
```

## 📱 Karing使用方法

1. 打开Karing应用
2. 点击"添加配置"或"订阅"
3. 选择"从URL导入"
4. 粘贴上面的订阅链接
5. 点击"更新订阅"

## ⚠️ 重要提示

- 免费节点稳定性较差,建议定期更新订阅
- 节点速度和可用性随时可能变化
- 建议在Karing中启用"自动选择"或"延迟测试"
- 仅供学习研究使用,请遵守当地法律法规

## 🔄 自动更新

本仓库使用GitHub Actions每2小时自动更新一次节点列表。

## 📝 说明

订阅数据来源于 [roosterkid/openproxylist](https://github.com/roosterkid/openproxylist)
"""
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    print("✓ 生成README文档")

def main():
    print("=" * 60)
    print("OpenProxyList 订阅生成器")
    print("=" * 60)
    
    # 获取节点
    proxies, raw_content, base64_content = fetch_proxies()
    
    if not proxies:
        print("⚠️  未获取到任何节点,保持原有文件不变")
        return
    
    # 保存订阅文件
    save_subscriptions(proxies, raw_content, base64_content)
    
    print("=" * 60)
    print("✅ 订阅更新完成!")
    print("=" * 60)

if __name__ == "__main__":
    main()
