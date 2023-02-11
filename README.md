# Aliyun Auto Signin

## 说明

项目用于自动实现阿里云盘的每日签到活动.

| 功能   | 是否支持 | 未来计划 |
|------|:----:|:----:|
| 签到   |  Y   |  -   |
| 签到推送 |  N   |  Y   |
| 多账户  |  N   |  N   |

_该项目不支持多账户同时签到, 且未来不会添加该功能. 如有需要请等待另一闭源签到平台的发布, 或部署多份代码同时运行._

## 使用方法

注意: main 分支仅支持 Python 3.10 及以上版本, 低于 3.10 的版本请移步 [低版本兼容分支](https://github.com/ImYrS/aliyun-auto-signin/tree/older-python-version)

1. Clone 本项目到本地或下载 Release 版本
2. 环境安装
    1. `Python >= 3.10`
    2. 安装依赖
        ```bash
        pip install configobj requests
        ```
3. 修改配置文件
    1. 复制 `example.config` 为 `config.ini`
    2. 在配置文件中填入你的阿里云盘 `refresh token`
4. 运行并查看是否成功签到
    ```bash
    python app.py
    ```
5. 使用任意方式每日定时运行 `app.py` 即可
6. 以 nohup 等后台形式运行时, 可在 自动生成的 `.log` 文件中查看运行日志

## 其他

- 欢迎在 [Issues](https://github.com/ImYrS/aliyun-auto-signin/issues) 中反馈问题
- PRs are welcome
