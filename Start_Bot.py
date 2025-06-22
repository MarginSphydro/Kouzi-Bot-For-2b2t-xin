import os
import subprocess

# ==== 配置 ====
max_bots = 20
exe_name = "MinecraftClient-20241227-281-win-x64.exe"

# ==== 输入数量 ====
try:
    count = int(input(f"你要启动几个 MCC 宣传机器人？(1~{max_bots}): ").strip())
    if count < 1 or count > max_bots:
        raise ValueError
except ValueError:
    print("请输入 1 到 20 之间的整数")
    exit(1)

# ==== 显示选项 ====
print("\n窗口显示选项：")
print("1 = 每个 bot 单独弹出控制台窗口（推荐）")
print("2 = 仅显示第 1 个窗口，其它后台运行")
print("3 = 全部后台静默运行（无窗口）")
mode = input("请选择窗口模式 (1/2/3): ").strip()

# ==== 启动 ====
base_dir = os.getcwd()
for i in range(1, count + 1):
    bot_dir = os.path.join(base_dir, str(i))
    exe_path = os.path.join(bot_dir, exe_name)

    if not os.path.isfile(exe_path):
        print(f"[跳过] 未找到：{exe_path}")
        continue

    if mode == "1":
        # 每个 bot 使用 start 命令打开新窗口运行
        cmd = f'start "MCC Bot {i}" "{exe_path}"'
        subprocess.Popen(cmd, cwd=bot_dir, shell=True)

    elif mode == "2":
        if i == 1:
            subprocess.Popen([exe_path], cwd=bot_dir)
        else:
            subprocess.Popen([exe_path], cwd=bot_dir, creationflags=subprocess.CREATE_NO_WINDOW)

    elif mode == "3":
        subprocess.Popen([exe_path], cwd=bot_dir, creationflags=subprocess.CREATE_NO_WINDOW)

    else:
        print("无效模式，默认使用静默模式。")
        subprocess.Popen([exe_path], cwd=bot_dir, creationflags=subprocess.CREATE_NO_WINDOW)

print(f"\n[完成] 启动 {count} 个机器人，窗口模式：{mode}")
