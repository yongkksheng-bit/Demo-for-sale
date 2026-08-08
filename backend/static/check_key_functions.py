with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 检查关键函数
functions = [
    "selectTool",
    "sendMessage",
    "generateSalesScript",
    "handleObjection",
    "generateCompetitorCompare",
    "generateVisitChecklist",
    "calculateROI",
    "showSection",
]

print("=== 关键函数检查 ===")
for func in functions:
    if f"function {func}" in content:
        print(f"✅ {func} 存在")
    else:
        print(f"❌ {func} 不存在！")

# 检查最后几行，看看是不是有代码被截断了
lines = content.split("\n")
print(f"\n总行数: {len(lines)}")
print("最后5行:")
for i in range(max(0, len(lines)-5), len(lines)):
    print(f"  {i+1}: {lines[i][:80]}")
