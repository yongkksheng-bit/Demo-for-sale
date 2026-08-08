with open("app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找到 selectTool 函数
for i, line in enumerate(lines):
    if "function selectTool" in line:
        print(f"selectTool 函数在第 {i+1} 行")
        print(f"  缩进: {len(line) - len(line.lstrip())} 个空格")
        
        # 检查是不是全局的
        brace_count = 0
        for j in range(i):
            brace_count += lines[j].count("{")
            brace_count -= lines[j].count("}")
        
        print(f"  大括号深度: {brace_count}")
        if brace_count == 0:
            print("  ✅ 是全局函数")
        else:
            print(f"  ❌ 不是全局函数，在第 {brace_count} 层作用域内")
        break
else:
    print("❌ 找不到 selectTool 函数")
