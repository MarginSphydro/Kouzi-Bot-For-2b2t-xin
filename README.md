# CombinedBot MCCScript README

> **v2.2 (最新) - 高光！自动答题功能**
>
> - 在队列题目中识别关键词并自动提交正确选项。
> - 支持 A, B, C, D 四个选项格式。

---

## 下载方式

由于 GitHub 单文件限制（25MB），请在 [Releases 页面](https://github.com/MarginSphydro/Kouzi-Bot-For-2b2t-xin/releases) 下载完整压缩包。

---

## 功能版本说明

### v2.2 (2025/6/28)

- **自动答题**：
  - 脚本会在聊天中检测包含“选项”的行，通过预设题库自动匹配并发送小写字母（`a`/`b`/`c`/`d`）。

---

### v2.1 (2025/6/22)

- 优化了自动启动脚本 `opener.py`：
  1. 双击 `opener.py` 即可快速启动指定数量的机器人。
  2. 编辑 `for i in range(1, 11):` 中的 `11` 为启动数量+1。
     - 例如修改为 `range(1, 21)` 可启动 20 个机器人。
- “Start\_Bot.py” 已废弃，请勿使用。
- `Mutil_Proxy_Editor.py`：用于导入代理，格式 `ip:port:username:password`，也可只写 `ip:port`。代理添加前请在 `proxy.txt`添加内容
- `AntiBlock_Username.py`：生成随机中文名字。
- `UserName.py`：根据输入前缀生成递增用户名，例如：当你输入 A1hen是我性奴
  ```
  A1hen是我性奴
  A1hen是我性奴1
  A1hen是我性奴2
  ...  
  ```
- 使用说明：
  1. 解压下载的压缩包，找到目录 `1`，复制并重命名为 `1` 到 `20`（共 20 个文件夹）。
  2. 在每个文件夹内修改 `login.cs`，添加机器人控制用户名，切勿删除 `mark_7601` 等默认用户名否则你将被我黑客入侵
  3. 前往 [聚凉 IP 代理](https://www.juliangip.com/user/reg?inviteCode=1052412) 获取付费代理。(如果你不用我的推广链接你同样的也会被我黑客入侵)

---

### v2.0

- 支持**游戏内指令**控制机器人发送内容：
  - `att <玩家名>` —— 使用侮辱词汇池轮询发送私聊或公开辱骂。
    ```
    <mark_7601> att A1hen  
    <bot> A1hen 草泥马的  
    <bot> A1hen 你是不是只会念三字经的  
    ...  
    ```
  - `attsimp <内容>` —— 重复发送单句内容。
    ```
    <mark_7601> attsimp 火速购买prism  
    <bot> 火速购买prism  
    <bot> 火速购买prism  
    ...  
    ```
  - `attmsg <玩家名>` —— 私聊侮辱玩家（词汇池）。
  - `attmsgsimp <玩家名> <内容>` —— 私聊重复发送指定消息。
  - `SK <任意内容>` —— 令机器人执行指令或发言。

---

> **注意**：请保留原有内容，不要擅自删除或修改默认设置，以免影响脚本稳定性。

---

© 2025 Margin Sphydro Team On Top

