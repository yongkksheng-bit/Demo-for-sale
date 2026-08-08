with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 方案生成：加上 bg-gray-50
content = content.replace(
    '<section id="solution" class="section hidden py-16">',
    '<section id="solution" class="section hidden py-16 bg-gray-50">'
)

# 销售工具箱：加上 bg-gray-50
content = content.replace(
    '<section id="tools" class="section hidden py-16">',
    '<section id="tools" class="section hidden py-16 bg-gray-50">'
)

# 检查智能对话的背景
idx = content.find('id="chat"')
if idx != -1:
    # 往前找 section
    section_start = content.rfind("<section", 0, idx)
    section_tag = content[section_start:section_start+200]
    print(f"智能对话 section: {section_tag[:100]}")
    
    # 如果没有 bg-gray-50，加上
    if "bg-gray-50" not in section_tag:
        # 找到 class
        import re
        match = re.search(r'class="([^"]*)"', section_tag)
        if match:
            old_class = match.group(1)
            new_class = old_class + " bg-gray-50"
            content = content[:section_start] + section_tag.replace(old_class, new_class) + content[section_start+len(section_tag):]
            print("✅ 已给智能对话加上 bg-gray-50")

# 保存
with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("\n✅ 已统一所有模块的背景颜色")
print("  - 方案生成：加上 bg-gray-50")
print("  - 销售工具箱：加上 bg-gray-50")
print("  - 所有模块背景保持一致")
