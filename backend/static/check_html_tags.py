with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

print(f"文件总长度: {len(content)} 字符")

# 检查 section 标签数量
import re
sections = re.findall(r'<section', content)
section_ends = re.findall(r'</section>', content)
print(f"<section> 开始标签: {len(sections)} 个")
print(f"</section> 结束标签: {len(section_ends)} 个")

# 检查 div 标签
divs = re.findall(r'<div', content)
div_ends = re.findall(r'</div>', content)
print(f"\n<div> 开始标签: {len(divs)} 个")
print(f"</div> 结束标签: {len(div_ends)} 个")

# 检查 button 标签
btns = re.findall(r'<button', content)
btn_ends = re.findall(r'</button>', content)
print(f"\n<button> 开始标签: {len(btns)} 个")
print(f"</button> 结束标签: {len(btn_ends)} 个")
