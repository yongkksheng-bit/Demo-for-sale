with open("app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找到 selectTool 函数
start = -1
for i, line in enumerate(lines):
    if "function selectTool" in line:
        start = i
        break

if start != -1:
    # 找函数结束
    brace_count = 0
    end = -1
    for i in range(start, len(lines)):
        brace_count += lines[i].count("{")
        brace_count -= lines[i].count("}")
        if brace_count == 0 and i > start:
            end = i
            break
    
    if end != -1:
        print(f"selectTool 函数从第 {start+1} 行到第 {end+1} 行")
        print("=== 函数内容 ===")
        for i in range(start, end+1):
            print(f"{i+1}: {lines[i].rstrip()}")
        
        # 检查有没有 calculateROI
        func_content = "".join(lines[start:end+1])
        if "calculateROI" in func_content:
            print("\n✅ 包含 calculateROI")
        else:
            print("\n❌ 不包含 calculateROI")
