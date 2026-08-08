with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 需要修复的函数和对应的请求体最后一个参数
fixes = [
    # 销售话术：最后一个参数是 scenario
    ("generateSalesScript", "scenario: scenario"),
    # 异议处理：最后一个参数是 industry
    ("handleObjection", "industry: industry"),
    # 竞品对比：最后一个参数是 scenario
    ("generateCompetitorCompare", "scenario: scenario"),
    # 拜访清单：最后一个参数是 position
    ("generateVisitChecklist", "position: position"),
]

for func_name, last_param in fixes:
    # 找到函数
    search_str = f"async function {func_name}"
    if search_str not in content:
        search_str = f"function {func_name}"
    
    idx = content.find(search_str)
    if idx == -1:
        print(f"❌ {func_name}: 函数不存在")
        continue
    
    # 找到 body: JSON.stringify({
    body_start = content.find("body: JSON.stringify({", idx)
    if body_start == -1:
        print(f"❌ {func_name}: 找不到请求体")
        continue
    
    # 找到最后一个参数的位置
    param_idx = content.find(last_param, body_start)
    if param_idx == -1:
        print(f"❌ {func_name}: 找不到参数 {last_param}")
        continue
    
    # 找到这个参数行的结束（换行）
    line_end = content.find("\n", param_idx)
    if line_end == -1:
        print(f"❌ {func_name}: 找不到行结束")
        continue
    
    # 在这个参数后面加上 identity 参数
    # 先看看这一行的缩进
    line_start = content.rfind("\n", 0, param_idx) + 1
    indent = content[line_start:param_idx]
    
    # 插入 identity 参数
    identity_line = f"\n{indent}identity: currentIdentity,"
    
    # 在最后一个参数后面插入
    content = content[:line_end] + identity_line + content[line_end:]
    
    print(f"✅ {func_name}: 已添加 identity 参数")

with open("app.js", "w", encoding="utf-8") as f:
    f.write(content)

print("\n所有修复完成！")
