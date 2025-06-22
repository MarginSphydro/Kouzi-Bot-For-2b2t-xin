import os
import re

# 配置
base_dir = os.getcwd()  # 或者替换为你的 mmc 根目录路径，如 "C:/mmcbots/"
username_prefix = input("请输入用户名前缀，例如 A1hen是我性奴：").strip()

# 遍历 1 到 20 号文件夹
for i in range(1, 31):
    folder = os.path.join(base_dir, str(i))
    ini_path = os.path.join(folder, "MinecraftClient.ini")

    if not os.path.isfile(ini_path):
        print(f"[警告] 跳过：未找到 {ini_path}")
        continue

    with open(ini_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 使用正则修改 Login 和 Password 字段
    new_username = f'{username_prefix}{i}'
    new_content = re.sub(
        r'Account\s*=\s*\{\s*Login\s*=\s*".*?",\s*Password\s*=\s*".*?"\s*\}',
        f'Account = {{ Login = "{new_username}", Password = "-" }}',
        content
    )

    # 写回文件
    with open(ini_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"[完成] {ini_path} → 用户名设置为 {new_username}")
