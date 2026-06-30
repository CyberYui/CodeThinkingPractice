# 标题一
## 标题二

普通段落，带**加粗**文字。
日常开发中推荐使用 **uv** 管理 Python 环境，搭配 *VS Code Pylint* 做代码校验；<span style="color:#2277cc">`~/.local/share/uv/python/3.11`</span> 是当前主力解释器。若出现 `subprocess.Popen` 启动报错，先执行 `proxyreset` 清空代理变量，再从干净终端 `code .` 重启编辑器，即可规避环境变量污染引发的 Linting 故障。

- 列表项1，普通列表
## 本地多Python环境资产对照表
| 环境归属 | Python版本 | 存放路径前缀 | 使用软件 |
|--------|-----------|-------------|---------|
| uv托管 | 3.11.15 | ~/.local/share/uv/python | VS Code Pylint、本地项目 |
| Homebrew全局 | 3.14.6 | /opt/homebrew/opt/python@3.14 | 终端默认python3、brew脚本 |
| Miniconda | 3.13.13 | /opt/homebrew/Caskroom/miniconda | OpenClaw、数据脚本 |
| macOS系统 | 3.9.6 | /usr/bin/python3 | Xcode、系统底层编译 |
| uv可选下载 | 3.15.0b2 | 无本地实体文件 | 仅预缓存版本，未安装 |
- 列表项2，多级无序列表
## Hermes Agent 安全运维操作清单
- 后台进程管理
  - 停止网关：`hermes gateway stop`
  - 卸载开机自启：`hermes service uninstall`
- QQ Bot 消息权限控制
  - 配对审批模式：陌生人私聊需终端放行
  - 仅白名单OpenID：手动录入允许访问的QQ账号
- LLM模型配置
  - DeepSeek V4-Pro 推理模型，开启高力度思考链
  - 密钥独立存储于 `~/.hermes/.env`
- 目录隔离规范
  - 禁止执行 `hermes claw cleanup`（会破坏OpenClaw）
  - 关闭自动扫描OpenClaw目录消除迁移弹窗
- 缓存磁盘清理
  - 扫描占用：`hermes disk-cleanup scan`
  - 一键清空图片/音频临时缓存

[链接](https://github.com)
python practice.py test.md