with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找包含 "填写客户信息" 的行
for i, line in enumerate(lines):
    if "填写客户信息" in line:
        print(f"第 {i+1} 行: {line.strip()[:80]}...")
        # 往前找5行
        for j in range(max(0, i-5), i):
            print(f"  第 {j+1} 行: {lines[j].strip()[:80]}...")
        break
