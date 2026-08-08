with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找到模态框的范围
modal_start = content.find('id="identity-modal"')
modal_end = content.find('</div>', modal_start + 500)  # 大概找一下
# 更准确一点，找到模态框的结束
# 模态框是一个大的 div，我们找到下一个 <!-- 注释或者下一个大的 section
modal_end = content.find('<!--', modal_start + 1000)
if modal_end == -1:
    modal_end = len(content)

modal_content = content[modal_start:modal_end]
print(f"模态框内 selectIndustry 调用次数: {modal_content.count('selectIndustry(')}")

# 把模态框里的 selectIndustry 改成 selectIdentityIndustry
new_modal_content = modal_content.replace("selectIndustry(", "selectIdentityIndustry(")
content = content[:modal_start] + new_modal_content + content[modal_end:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ HTML 里身份选择的行业按钮已改名为 selectIdentityIndustry")

# 验证一下
print(f"\n验证:")
print(f"  总 selectIndustry 调用次数: {content.count('selectIndustry(')}")
print(f"  总 selectIdentityIndustry 调用次数: {content.count('selectIdentityIndustry(')}")
