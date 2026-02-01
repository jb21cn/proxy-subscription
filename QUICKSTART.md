# 🚀 5分钟快速部署指南

## 步骤1: 创建GitHub仓库 (1分钟)

1. 登录GitHub: https://github.com
2. 点击右上角的 "+" → "New repository"
3. 仓库名称: `proxy-subscription` (可以自定义)
4. 选择 "Public" (公开仓库)
5. 点击 "Create repository"

## 步骤2: 上传文件 (2分钟)

### 方法A: 通过网页上传

1. 在新创建的仓库页面,点击 "uploading an existing file"
2. 将本地的所有文件拖拽到上传区域:
   - `.github/` 文件夹
   - `scripts/` 文件夹
   - `SETUP.md`
   - `requirements.txt`
   - `.gitignore`
3. 在底部填写提交信息: "Initial commit"
4. 点击 "Commit changes"

### 方法B: 使用Git命令行

```bash
# 在项目目录下执行
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/proxy-subscription.git
git push -u origin main
```

## 步骤3: 配置GitHub Actions (1分钟)

1. 进入仓库的 **Settings** 标签页
2. 左侧菜单选择 **Actions** → **General**
3. 在 "Workflow permissions" 部分:
   - 选择 ✅ **"Read and write permissions"**
   - 勾选 ✅ **"Allow GitHub Actions to create and approve pull requests"**
4. 点击 **Save** 保存

## 步骤4: 运行首次更新 (1分钟)

1. 进入仓库的 **Actions** 标签页
2. 选择左侧的 **"更新代理订阅"** workflow
3. 点击右侧的 **"Run workflow"** 按钮
4. 在弹出菜单中再次点击绿色的 **"Run workflow"** 按钮
5. 等待约1-2分钟,直到显示绿色的 ✅

## 步骤5: 获取订阅链接 (30秒)

1. 回到仓库首页
2. 进入 `subscriptions` 文件夹
3. 点击 `v2ray_base64.txt` 文件
4. 点击右侧的 **"Raw"** 按钮
5. 复制浏览器地址栏的URL,这就是你的订阅链接!

**订阅链接格式:**
```
https://raw.githubusercontent.com/YOUR_USERNAME/proxy-subscription/main/subscriptions/v2ray_base64.txt
```

## 步骤6: 在Karing中使用

1. 打开Karing应用
2. 点击 "添加配置" 或 "+"
3. 选择 "从URL导入" 或 "订阅链接"
4. 粘贴你的订阅链接
5. 点击 "确定" 和 "更新订阅"
6. 完成!

## 🎉 大功告成!

现在你的订阅会每2小时自动更新一次。你可以:

- ✅ 在Karing中定期"更新订阅"获取最新节点
- ✅ 随时在Actions页面手动触发更新
- ✅ 修改 `.github/workflows/update-subscription.yml` 调整更新频率

## ⚠️ 常见问题

**Q: Actions执行失败?**
- 检查Step 3的权限设置是否正确
- 查看Actions日志了解具体错误

**Q: 订阅链接打不开?**
- 确保仓库是Public的
- 确认链接中的用户名和仓库名正确
- 可以使用GitHub代理: `ghproxy.com` 或 `fastgit.org`

**Q: 如何修改更新频率?**
- 编辑 `.github/workflows/update-subscription.yml`
- 修改 `cron: '0 */2 * * *'` 这一行
- 例如改成 `'0 */6 * * *'` 表示每6小时更新

## 📞 需要帮助?

如有问题,欢迎在仓库中提Issue!
