with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找 "销售工具箱" 文字
for i, line in enumerate(lines):
    if "销售工具箱" in line and "nav-item" not in line:
        print(f"销售工具箱文字在第 {i+1} 行: {line.strip()[:80]}")
        # 往前找5行
        for j in range(max(0, i-5), i):
            if "<section" in lines[j]:
                print(f"  section 开始在第 {j+1} 行: {lines[j].strip()[:80]}")
        break

# 找 "智能对话" 文字（不是侧边栏的）
for i, line in enumerate(lines):
    if "智能对话顾问" in line:
        print(f"\n智能对话文字在第 {i+1} 行: {line.strip()[:80]}")
        break
