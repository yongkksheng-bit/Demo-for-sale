with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 第807行：saveCustomer 按钮
line_idx = 806  # 索引从0开始
line = lines[line_idx]
print(f"第807行原内容: {line.strip()[:80]}...")

# 替换样式
new_line = line.replace("bg-gradient-primary", "bg-white border border-gray-200 text-gray-900 shadow-sm")
new_line = new_line.replace("text-white", "text-gray-900")
lines[line_idx] = new_line
print("✅ 保存客户按钮已修改")

# 第852行：saveFollowUp 按钮
line_idx2 = 851
line2 = lines[line_idx2]
print(f"\n第852行原内容: {line2.strip()[:80]}...")

new_line2 = line2.replace("bg-gradient-primary", "bg-white border border-gray-200 text-gray-900 shadow-sm")
new_line2 = new_line2.replace("text-white", "text-gray-900")
lines[line_idx2] = new_line2
print("✅ 保存跟进按钮已修改")

with open("index.html", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("\n✅ 所有渐变按钮都已改成白色样式")
