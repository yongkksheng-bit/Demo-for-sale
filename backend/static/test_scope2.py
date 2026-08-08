with open("app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 从文件开头统计 { 和 } 的数量，到第746行（showIdentityModal函数定义）时，看看brace_count是多少
brace_count = 0
func_line_idx = 745  # 第746行，索引745

for i in range(func_line_idx):
    line = lines[i]
    # 简单统计，不考虑字符串里的括号
    brace_count += line.count("{")
    brace_count -= line.count("}")

print(f"到第746行时，大括号深度: {brace_count}")
if brace_count == 0:
    print("✅ 函数是全局的")
else:
    print(f"❌ 函数在第{brace_count}层作用域内，不是全局的")
    # 找到最近的外层函数
    depth = brace_count
    for i in range(func_line_idx - 1, -1, -1):
        line = lines[i]
        depth -= line.count("{")
        depth += line.count("}")
        if depth == 0 and "function" in line:
            print(f"外层函数在第 {i+1} 行: {line.strip()}")
            break
