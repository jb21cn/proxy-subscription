# 🚀 Karing 自动代理订阅服务

[![Update Proxies](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/update-subscription.yml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/update-subscription.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> 自动从 [openproxylist.com](https://openproxylist.com) 抓取免费V2Ray节点,生成Karing兼容的订阅文件

## ✨ 特性

- 🔄 **自动更新**: 使用GitHub Actions每2小时自动抓取最新节点
- 📱 **多格式支持**: 提供V2Ray、Clash等多种订阅格式
- 🆓 **完全免费**: 基于GitHub Actions,无需服务器
- 🚀 **即开即用**: 一键部署,5分钟搞定
- 🔒 **安全可靠**: 代码开源透明,数据来源可信

## 📖 使用文档

- [📘 完整部署指南](SETUP.md) - 详细的部署说明
- [⚡ 5分钟快速开始](QUICKSTART.md) - 最简洁的部署步骤

## 🔗 订阅链接

部署完成后,你将获得以下订阅链接:

### V2Ray订阅 (推荐)
```
https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/subscriptions/v2ray_base64.txt
```

### Clash订阅
```
https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/subscriptions/clash.yaml
```

> ⚠️ 请将 `YOUR_USERNAME` 和 `YOUR_REPO` 替换为你的GitHub用户名和仓库名

## 🎯 在Karing中使用

1. 打开Karing应用
2. 添加订阅 → 从URL导入
3. 粘贴订阅链接
4. 更新订阅即可使用

详细使用说明请查看 [SETUP.md](SETUP.md#5-在karing中使用)

## 📊 项目结构

```
proxy-subscription/
├── .github/workflows/
│   └── update-subscription.yml    # 自动更新配置
├── scripts/
│   └── update_proxies.py          # 节点抓取脚本
├── subscriptions/                  # 订阅文件(自动生成)
│   ├── v2ray_base64.txt           # V2Ray Base64订阅
│   ├── v2ray.txt                  # V2Ray纯文本订阅
│   ├── clash.yaml                 # Clash订阅配置
│   └── stats.json                 # 统计信息
├── SETUP.md                        # 详细部署指南
├── QUICKSTART.md                   # 快速开始指南
└── README.md                       # 项目说明(本文件)
```

## ⚙️ 自定义配置

### 修改更新频率

编辑 `.github/workflows/update-subscription.yml`:

```yaml
schedule:
  - cron: '0 */2 * * *'  # 每2小时更新一次
```

常用设置:
- 每小时: `'0 * * * *'`
- 每6小时: `'0 */6 * * *'`
- 每天: `'0 0 * * *'`

### 手动更新

前往仓库的 Actions 页面,选择 "更新代理订阅",点击 "Run workflow" 即可手动触发更新。

## ⚠️ 重要提示

- 本项目提供的节点来自公共代理池,**稳定性和速度无法保证**
- 免费节点可能随时失效,建议经常更新订阅
- 不建议在公共节点上传输敏感信息
- **仅供学习研究使用**,请遵守当地法律法规

## 🔧 故障排除

### GitHub Actions运行失败
1. 检查仓库的Actions权限设置(Settings → Actions → General)
2. 确保选择了 "Read and write permissions"
3. 查看Actions日志了解具体错误

### 订阅链接无法访问
1. 确认仓库是Public(公开)的
2. 检查链接中的用户名和仓库名是否正确
3. 可以使用GitHub代理服务,如 `ghproxy.com`

### Karing导入订阅失败
1. 使用 `v2ray_base64.txt` 而非 `v2ray.txt`
2. 检查订阅链接是否完整
3. 在Karing中尝试手动更新订阅

更多问题请查看 [SETUP.md](SETUP.md#-故障排除)

## 🌟 数据来源

本项目的节点数据来自:
- [openproxylist.com](https://openproxylist.com)
- [roosterkid/openproxylist](https://github.com/roosterkid/openproxylist)

## 📝 许可证

[MIT License](LICENSE)

## 🤝 贡献

欢迎提交Issue和Pull Request!

如果这个项目对你有帮助,请给一个 ⭐ Star 支持一下!

## 📧 联系方式

如有问题或建议,欢迎:
- 提交 [Issue](../../issues)
- 提交 [Pull Request](../../pulls)

---

**免责声明**: 本项目仅供学习交流使用,请勿用于违法用途。使用本项目所产生的一切后果由使用者自行承担。
