# OpenProxyList 自动订阅服务

自动从 [openproxylist.com](https://openproxylist.com) 抓取免费V2Ray节点,并生成Karing兼容的订阅文件。

## 🚀 快速开始

### 1. Fork或创建仓库

1. 在GitHub上创建一个新仓库(例如: `proxy-subscription`)
2. 将本项目的所有文件上传到你的仓库

### 2. 启用GitHub Actions

1. 进入你的仓库 Settings → Actions → General
2. 确保 "Allow all actions and reusable workflows" 已启用
3. 在 Workflow permissions 中选择 "Read and write permissions"
4. 保存设置

### 3. 手动触发首次更新

1. 进入仓库的 Actions 标签页
2. 选择 "更新代理订阅" workflow
3. 点击 "Run workflow" → "Run workflow" 按钮
4. 等待执行完成(约1-2分钟)

### 4. 获取订阅链接

执行完成后,在仓库中会生成 `subscriptions` 目录,包含以下订阅文件:

**V2Ray Base64订阅** (推荐用于Karing):
```
https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/subscriptions/v2ray_base64.txt
```

**V2Ray纯文本订阅**:
```
https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/subscriptions/v2ray.txt
```

**Clash订阅**:
```
https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/subscriptions/clash.yaml
```

> ⚠️ 记得将 `YOUR_USERNAME` 和 `YOUR_REPO` 替换为你的GitHub用户名和仓库名!

### 5. 在Karing中使用

#### 方法一: 直接导入URL
1. 打开Karing
2. 点击 "+" 或 "添加配置"
3. 选择 "URL" 或 "订阅链接"
4. 粘贴订阅链接
5. 点击"保存"和"更新订阅"

#### 方法二: 如果Karing支持GitHub订阅
1. 打开Karing
2. 选择 "GitHub订阅"
3. 输入: `YOUR_USERNAME/YOUR_REPO`
4. 分支: `main`
5. 路径: `subscriptions/v2ray_base64.txt`

## ⚙️ 配置说明

### 修改更新频率

编辑 `.github/workflows/update-subscription.yml` 文件中的 cron 表达式:

```yaml
schedule:
  - cron: '0 */2 * * *'  # 每2小时更新一次
```

常用时间设置:
- `0 */1 * * *` - 每1小时
- `0 */6 * * *` - 每6小时  
- `0 0 * * *` - 每天0点

### 手动触发更新

随时可以在 Actions 页面手动运行 workflow 来更新节点。

## 📁 项目结构

```
proxy-subscription/
├── .github/
│   └── workflows/
│       └── update-subscription.yml  # GitHub Actions配置
├── scripts/
│   └── update_proxies.py           # 节点抓取脚本
├── subscriptions/                   # 生成的订阅文件(自动创建)
│   ├── v2ray_base64.txt
│   ├── v2ray.txt
│   ├── clash.yaml
│   └── stats.json
└── README.md
```

## 🔍 故障排除

### Actions运行失败

1. 检查仓库的Actions权限设置
2. 查看Actions运行日志了解具体错误
3. 确保网络能访问 `raw.githubusercontent.com`

### 订阅链接无法访问

1. 确认文件已经生成在 `subscriptions` 目录
2. 检查仓库是否为Public(私有仓库需要token)
3. 尝试使用 `ghproxy.com` 等GitHub代理服务

### Karing无法导入订阅

1. 确认使用的是正确的订阅链接格式
2. 尝试使用 `v2ray_base64.txt` 而不是 `v2ray.txt`
3. 检查Karing的UserAgent设置

## ⚠️ 重要提示

- **稳定性**: 免费公共节点稳定性较差,可能随时失效
- **速度**: 公共节点通常速度较慢且不稳定
- **隐私**: 不建议在公共节点上传输敏感信息
- **用途**: 仅供学习研究使用,请遵守当地法律法规

## 🔗 相关链接

- [openproxylist.com](https://openproxylist.com)
- [roosterkid/openproxylist](https://github.com/roosterkid/openproxylist)
- [Karing官网](https://karing.app)
- [GitHub Actions文档](https://docs.github.com/actions)

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request!
