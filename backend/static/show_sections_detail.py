with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 1. 找三步上手（输入客户信息）
print("=== 1. 三步上手部分 ===")
for i, line in enumerate(lines):
    if "输入客户信息" in line:
        # 往前找15行，看看有没有"三步"
        for j in range(max(0, i-20), i):
            if "三步" in lines[j] or "3步" in lines[j]:
                start = max(0, i-15)
                end = min(len(lines), i+40)
                for k in range(start, end):
                    print(f"  {k+1}: {lines[k].rstrip()[:90]}")
                break
        break

print("\n" + "="*60)

# 2. 找方案生成的步骤指示器
print("\n=== 2. 方案生成步骤指示器 ===")
for i, line in enumerate(lines):
    if "你卖什么？" in line:
        start = max(0, i-10)
        end = min(len(lines), i+10)
        for j in range(start, end):
            print(f"  {j+1}: {lines[j].rstrip()[:90]}")
        break

print("\n" + "="*60)

# 3. 销售工具箱的开头
print("\n=== 3. 销售工具箱开头 ===")
for i, line in enumerate(lines):
    if 'id="tools"' in line:
        start = i
        end = min(len(lines), i+30)
        for j in range(start, end):
            print(f"  {j+1}: {lines[j].rstrip()[:90]}")
        break
