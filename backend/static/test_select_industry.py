with open("app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找到所有 selectIndustry 函数定义
print("=== selectIndustry 函数定义位置 ===\n")
for i, line in enumerate(lines):
    if "function selectIndustry" in line:
        print(f"第 {i+1} 行: {line.strip()}")
        # 看看后面几行，大概知道是干什么的
        for j in range(i+1, min(i+10, len(lines))):
            print(f"  {lines[j].strip()}")
        print()
