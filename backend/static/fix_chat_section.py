with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 第1165行（索引1164）是智能对话的section开始，但是不完整
print(f"修复前第1165行: {lines[1164].rstrip()}")

# 修复：加上 <section
lines[1164] = '        <section id="chat" class="section hidden py-16 bg-gray-50">\n'

print(f"修复后第1165行: {lines[1164].rstrip()}")

# 保存
with open("index.html", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("\n✅ 已修复智能对话的 section 标签")
print("  - 加上 <section 开头")
print("  - 加上 bg-gray-50 背景，和其他模块一致")
