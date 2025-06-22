import os
import subprocess
import time

def main():
    try:
        delay = float(input("请输入每次启动间隔时间（秒）："))
    except ValueError:
        print("输入无效，请输入数字")
        return

    root = os.getcwd()

    for i in range(1, 11):
        folder = os.path.join(root, str(i))
        exe = "MinecraftClient-20241227-281-win-x64.exe"
        exe_path = os.path.join(folder, exe)

        if os.path.exists(exe_path):
            print(f"启动第 {i} 个实例：{exe_path}")
            # /min 参数：最小化窗口启动
            subprocess.Popen(
                f'start "Client {i}" /min cmd /c "cd /d \"{folder}\" && \"{exe}\""',
                shell=True
            )
        else:
            print(f"未找到：{exe_path}，跳过。")

        time.sleep(delay)

if __name__ == "__main__":
    main()
