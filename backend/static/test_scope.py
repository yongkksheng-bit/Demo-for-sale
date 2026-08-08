with open("app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 检查 showIdentityModal 函数前面的缩进
# 如果缩进是 0，说明是全局函数；如果有缩进，说明是在某个函数里面
func_line_idx = 745  # 第746行，索引745
line = lines[func_line_idx]
indent = len(line) - len(line.lstrip())
print(f"showIdentityModal 函数缩进: {indent} 个空格")
print(f"函数行: {line.strip()}")

# 往前找，看看是不是在某个大的函数里面
# 统计前面的 { 和 } 的数量
brace_count = 0
for i in range(func_line_idx - 1, -1, -1):
    line = lines[i]
    brace_count += line.count("}")
    brace_count -= line.count("{")
    if brace_count > 0:
        # 找到了对应的 {
        print(f"\n在第 {i+1} 行找到一个 {{，说明函数在另一个作用域内")
        print(f"那一行: {lines[i].strip()}")
        break

if brace_count <= 0:
    print("\n✅ 函数是全局的")
