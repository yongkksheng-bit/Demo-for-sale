with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找 id="tools"
for i, line in enumerate(lines):
    if 'id="tools"' in line:
        print(f"id=\"tools\" 在第 {i+1} 行: {line.strip()[:80]}")
        # 往前找3行
        for j in range(max(0, i-3), i):
            print(f"  第 {j+1} 行: {lines[j].rstrip()[:80]}")
        break

# 找第1214行附近，看看是不是 solution section 结束
print(f"\n第1213-1217行：")
for i in range(1212, 1217):
    if i < len(lines):
        print(f"  第 {i+1} 行: {lines[i].rstrip()[:80]}")
