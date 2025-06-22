#!/usr/bin/env python3
# batch_from_proxy_list.py

import os
import sys

VALID_PROXY_TYPES = ["HTTP", "SOCKS4", "SOCKS4A", "SOCKS5"]

def correct_proxy_type(ptype: str) -> str:
    ptype = ptype.strip().upper()
    for valid in VALID_PROXY_TYPES:
        if ptype == valid:
            return valid
    if "HTTP" in ptype:
        return "HTTP"
    if "SOCKS4A" in ptype:
        return "SOCKS4A"
    if "SOCKS4" in ptype:
        return "SOCKS4"
    if "SOCKS5" in ptype or "SOCK" in ptype:
        return "SOCKS5"
    return "SOCKS5"

def update_proxy_config(bot_dir, host, port, username, password, proxy_type="SOCKS5"):
    ini_path = os.path.join(bot_dir, "MinecraftClient.ini")
    if not os.path.isfile(ini_path):
        print(f"[跳过] 未找到：{ini_path}")
        return

    with open(ini_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    proxy_type = correct_proxy_type(proxy_type)

    # 删除非 [Proxy] 段落中的重复 Enabled_ 开头字段
    in_proxy = False
    cleaned_lines = []
    for line in lines:
        if line.strip().startswith('['):
            in_proxy = line.strip().lower() == '[proxy]'
        if not in_proxy and (
            line.strip().startswith("Enabled_Login =") or line.strip().startswith("Enabled_Ingame =")
        ):
            continue
        cleaned_lines.append(line)
    lines = cleaned_lines

    # 在 Proxy 区域（130~150）替换字段
    proxy_fields = {
        "Server":    f'Server = {{ Host = "{host}", Port = {port} }} # 代理服务器必须允许HTTPS登录。\n',
        "Proxy_Type": f'Proxy_Type = "{proxy_type}"                       # 支持的代理类型："HTTP"，"SOCKS4"，"SOCKS4a"，"SOCKS5"。\n',
        "Enabled_Update": 'Enabled_Update = false                      # 下载MCC的更新时是否通过代理服务器。\n',
        "Enabled_Login":  'Enabled_Login = true                        # 是否使用代理连接Mojang或微软的登录服务器。\n',
        "Enabled_Ingame": 'Enabled_Ingame = true                       # 是否通过代理连接Minecraft游戏服务器。\n',
        "Username":  f'Username = "{username}"                               # 只有连接到受密码保护的代理才需要。\n',
        "Password":  f'Password = "{password}"                               # 只有连接到受密码保护的代理才需要。\n'
    }

    keys_updated = set()
    for i in range(len(lines)):
        if 129 <= i <= 149:
            for key, new_line in proxy_fields.items():
                if lines[i].strip().startswith(f"{key} ") and key not in keys_updated:
                    lines[i] = new_line
                    keys_updated.add(key)

    # 添加缺失字段
    for key, new_line in proxy_fields.items():
        if key not in keys_updated:
            lines.append(new_line)

    with open(ini_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print(f"[完成] {ini_path} => {host}:{port} (用户: {username})")

def main():
    try:
        count = int(input("请输入要导入的代理数量（例如 10 表示 1~10）："))
        assert count > 0
    except:
        print("❌ 输入无效，请输入正整数")
        return

    if not os.path.isfile("proxy.txt"):
        print("❌ 未找到 proxy.txt 文件")
        return

    with open("proxy.txt", 'r', encoding='utf-8') as f:
        proxies = [line.strip() for line in f.readlines() if line.strip()]

    if len(proxies) < count:
        print(f"❌ proxy.txt 中只有 {len(proxies)} 条代理，无法分配 {count} 个")
        return

    for i in range(1, count + 1):
        proxy = proxies[i - 1]
        parts = proxy.split(':')
        if len(parts) != 4:
            print(f"[跳过] 第{i}行代理格式错误：{proxy}")
            continue

        host, port, username, password = parts
        update_proxy_config(str(i), host, port, username, password, "SOCKS5")

    print(f"\n✅ 已完成前 {count} 个目录的代理导入")

if __name__ == "__main__":
    main()
