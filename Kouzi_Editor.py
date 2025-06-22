# fill_insults_batch.py
import os

def load_cihui(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def generate_insult_lines(cihui_list):
    # 每一行为一个 C# 字符串
    return [f'"{line}"' for line in cihui_list]

def replace_insults_section(file_path, new_insults_lines):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    start_idx = end_idx = -1
    for i, line in enumerate(lines):
        if 'private string[] insults' in line:
            start_idx = i
            break

    if start_idx == -1:
        print(f"[跳过] 未找到 insults 段落：{file_path}")
        return False

    for j in range(start_idx + 1, len(lines)):
        if lines[j].strip().endswith("};"):
            end_idx = j
            break

    if end_idx == -1:
        print(f"[跳过] 未找到 insults 数组结束：{file_path}")
        return False

    # 构造替换块
    prefix = lines[start_idx].split('{')[0] + "{\n"
    new_block = [prefix]
    for line in new_insults_lines[:-1]:
        new_block.append("        " + line + ",\n")
    new_block.append("        " + new_insults_lines[-1] + "\n")
    new_block.append("    };\n")

    new_lines = lines[:start_idx] + new_block + lines[end_idx + 1:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    return True

def main():
    if not os.path.isfile("CiHui.txt"):
        print("❌ 未找到 CiHui.txt 文件")
        return

    cihui_list = load_cihui("CiHui.txt")
    insult_lines = generate_insult_lines(cihui_list)

    success = 0
    for i in range(1, 31):
        folder = str(i)
        login_path = os.path.join(folder, "login.cs")
        if os.path.isfile(login_path):
            if replace_insults_section(login_path, insult_lines):
                print(f"[完成] 写入 {login_path}")
                success += 1
        else:
            print(f"[跳过] 未找到：{login_path}")

    print(f"\n✅ 共修改 {success} 个 login.cs 文件")

if __name__ == "__main__":
    main()
