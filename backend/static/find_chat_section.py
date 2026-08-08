with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找"智能对话"文字在哪一行
for i, line in enumerate(lines):
    if "智能对话" in line and "nav-item" not in line:
        print(f"第 {i+1} 行: {line.strip()[:80]}...")
        # 往前找10行，看看有没有 section 标签
        for j in range(max(0, i-10), i):
            if "<section" in lines[j]:
                print(f"  第 {j+1} 行: {lines[j].strip()[:80]}...")
        break
