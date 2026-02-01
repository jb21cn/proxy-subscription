#!/bin/bash

echo "=================================="
echo "  代理订阅本地测试"
echo "=================================="
echo ""

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    echo "❌ 未找到Python3,请先安装Python"
    exit 1
fi

echo "✓ Python已安装"

# 安装依赖
echo ""
echo "正在安装依赖..."
pip3 install -q requests pyyaml

# 运行脚本
echo ""
echo "正在获取节点..."
python3 scripts/update_proxies.py

echo ""
echo "=================================="
echo "  测试完成!"
echo "=================================="
echo ""
echo "生成的文件位于 subscriptions/ 目录:"
echo "  - v2ray_base64.txt (Base64编码)"
echo "  - v2ray.txt (纯文本)"
echo "  - clash.yaml (Clash配置)"
echo "  - stats.json (统计信息)"
echo ""
