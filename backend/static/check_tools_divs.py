with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找销售工具箱 section 的开始和结束
tools_start = content.find('id="tools"')
# 往前找 section 开始
section_start = content.rfind("<section", 0, tools_start)
# 找结束
section_end = content.find("</section>", tools_start)

tools_content = content[section_start:section_end]

# 统计 div 数量
import re
divs = len(re.findall(r'<div', tools_content))
div_ends = len(re.findall(r'</div>', tools_content))
print(f"销售工具箱 section 内:")
print(f"  <div> 开始标签: {divs} 个")
print(f"  </div> 结束标签: {div_ends} 个")
print(f"  差值: {div_ends - divs} 个")

if div_ends != divs:
    print("❌ div 标签不对等！")
else:
    print("✅ div 标签对等")
