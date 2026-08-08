with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 第1489行（索引1488）是多余的
print("删除前，第1487-1491行：")
for i in range(1486, 1491):
    print(f"  {i+1}: {lines[i].rstrip()}")

# 删除第1489行（索引1488）
del lines[1488]

print("\n删除后，第1487-1491行：")
for i in range(1486, 1491):
    if i < len(lines):
        print(f"  {i+1}: {lines[i].rstrip()}")

# 检查 div 数量
divs = 0
div_ends = 0
for line in lines:
    divs += line.count("<div")
    div_ends += line.count("</div>")

print(f"\n全站 div 标签: 开始 {divs}, 结束 {div_ends}, 差值 {div_ends - divs}")
if divs == div_ends:
    print("✅ div 标签完全对等！")

# 保存
with open("index.html", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("\n✅ 已删除多余的 </div>")
