with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re

# 检查 section 数量
sections = len(re.findall(r'<section', content))
section_ends = len(re.findall(r'</section>', content))

print(f"全站 section 标签:")
print(f"  开始标签: {sections} 个")
print(f"  结束标签: {section_ends} 个")
print(f"  差值: {section_ends - sections} 个")

if sections == section_ends:
    print("✅ section 标签完全对等！")
else:
    print("❌ section 标签不对等")

# 检查 div 数量
divs = len(re.findall(r'<div', content))
div_ends = len(re.findall(r'</div>', content))

print(f"\n全站 div 标签:")
print(f"  开始标签: {divs} 个")
print(f"  结束标签: {div_ends} 个")
print(f"  差值: {div_ends - divs} 个")

if divs == div_ends:
    print("✅ div 标签完全对等！")
else:
    print("❌ div 标签不对等")
