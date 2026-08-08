with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找步骤指示器
print("=== 方案生成步骤指示器 ===")
for i, line in enumerate(lines):
    if "步骤指示器" in line:
        start = i
        # 找结束位置（找下一个大的 div 结束）
        end = min(len(lines), i + 50)
        for j in range(start, end):
            print(f"  {j+1}: {lines[j].rstrip()[:90]}")
        break
