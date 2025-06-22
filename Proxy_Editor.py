#!/usr/bin/env python3
# edit_proxy_interactive.py

import os

VALID_PROXY_TYPES = ["HTTP", "SOCKS4", "SOCKS4A", "SOCKS5"]

def correct_proxy_type(ptype: str) -> str:
    p = ptype.strip().upper()
    if p in VALID_PROXY_TYPES:
        return p
    if "SOCKS4A" in p:
        return "SOCKS4A"
    if "SOCKS4" in p:
        return "SOCKS4"
    if "SOCKS5" in p or "SOCK" in p:
        return "SOCKS5"
    return "SOCKS5"

def update_proxy_config(bot_dir, host, port, proxy_type):
    ini_path = os.path.join(bot_dir, "MinecraftClient.ini")
    if not os.path.isfile(ini_path):
        print(f"[跳过] 未找到：{ini_path}")
        return

    with open(ini_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    proxy_type = correct_proxy_type(proxy_type)

    # 删除非 [Proxy] 区段的 Enabled_Login/Enabled_Ingame
    in_proxy = False
    cleaned = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('['):
            in_proxy = stripped.lower() == '[proxy]'
        if not in_proxy and (stripped.startswith("Enabled_Login") or stripped.startswith("Enabled_Ingame")):
            continue
        cleaned.append(line)
    lines = cleaned

    # 要写入的 [Proxy] 字段
    proxy_fields = {
        "Server":         f'Server = {{ Host = "{host}", Port = {port} }} # 代理必须允许 HTTPS\n',
        "Proxy_Type":     f'Proxy_Type = "{proxy_type}"                       # 支持：HTTP, SOCKS4, SOCKS4a, SOCKS5\n',
        "Enabled_Update": 'Enabled_Update = false                      # 代理更新下载\n',
        "Enabled_Login":  'Enabled_Login = true                        # 代理登录认证\n',
        "Enabled_Ingame": 'Enabled_Ingame = true                       # 代理游戏连接\n',
        "Username":       'Username = ""                               # 代理用户名（无需可留空）\n',
        "Password":       'Password = ""                               # 代理密码（无需可留空）\n'
    }

    # 在 [Proxy] 段内替换或补充字段
    in_proxy = False
    updated = set()
    for idx, line in enumerate(lines):
        if line.strip().startswith('['):
            in_proxy = line.strip().lower() == '[proxy]'
        if in_proxy:
            for key, new_line in proxy_fields.items():
                if line.strip().startswith(f"{key} ") and key not in updated:
                    lines[idx] = new_line
                    updated.add(key)

    # 补充缺失字段
    if updated != set(proxy_fields.keys()):
        # 找到下一个区块开始的位置
        insert_at = len(lines)
        for idx, line in enumerate(lines):
            if line.strip().startswith('[') and line.strip().lower() != '[proxy]':
                insert_at = idx
                break
        for key, new_line in proxy_fields.items():
            if key not in updated:
                lines.insert(insert_at, new_line)
                insert_at += 1

    with open(ini_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print(f"[完成] 已更新 {bot_dir}/MinecraftClient.ini → {host}:{port} ({proxy_type})")

def main():
    print("=== MCC 代理配置修改工具 ===")
    dir_no = input("请输入要修改的子目录编号（如 1）: ").strip()
    hp = input("请输入代理地址 host:port（如 8.8.8.8:1080）: ").strip()
    proxy_type = input("请输入协议类型（HTTP/SOCKS4/SOCKS5），回车默认 SOCKS5: ").strip() or "SOCKS5"

    try:
        host, port = hp.split(':', 1)
    except ValueError:
        print("错误：代理地址格式应为 host:port")
        input("按回车键退出…")
        return

    bot_dir = os.path.join(os.getcwd(), dir_no)
    update_proxy_config(bot_dir, host, port, proxy_type)

    input("按回车键退出…")

if __name__ == "__main__":
    main()
