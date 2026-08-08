with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 先全部改回 selectIndustry
content = content.replace("selectIdentityIndustry(", "selectIndustry(")

# 现在，只改身份选择里的（有 industry-option 类的按钮）
# 找到所有包含 industry-option 并且有 selectIndustry 的行
lines = content.split("\n")
count = 0
new_lines = []
for line in lines:
    if "industry-option" in line and "selectIndustry(" in line:
        line = line.replace("selectIndustry(", "selectIdentityIndustry(")
        count += 1
    new_lines.append(line)

content = "\n".join(new_lines)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ 已修改 {count} 个身份选择的行业按钮")
print(f"   剩余 selectIndustry 调用: {content.count('selectIndustry(')}")
print(f"   selectIdentityIndustry 调用: {content.count('selectIdentityIndustry(')}")
