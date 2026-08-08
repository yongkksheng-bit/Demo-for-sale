with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. 先修复下拉框的bug - 把错误替换的"请你卖什么？"改回来
# 客户背调的行业下拉框默认选项
content = content.replace("请你卖什么？（可选）", "请选择行业")
content = content.replace("你卖什么？（可选）", "请选择行业")

# 2. 找到客户背调生成按钮的实际样式
research_start = content.find("id=\"research\"")
research_end = content.find("</section>", research_start)
research_content = content[research_start:research_end]

# 找生成按钮
import re
btn_match = re.search(r'<button[^>]*generateResearch[^>]*>', research_content)
if btn_match:
    print("客户背调生成按钮实际样式：")
    print(f"  {btn_match.group()[:150]}...")
    
    # 替换按钮样式
    old_btn = btn_match.group()
    # 提取 onclick 和其他属性
    onclick_match = re.search(r'onclick="[^"]*"', old_btn)
    onclick = onclick_match.group() if onclick_match else 'onclick="generateResearch()"'
    
    new_btn = f'<button {onclick} class="w-full py-3 bg-white border border-gray-200 text-gray-900 rounded-xl hover:bg-gray-50 hover:shadow-md transition-all font-medium shadow-sm flex items-center justify-center space-x-2">'
    
    # 找到按钮结束标签
    btn_end_match = re.search(r'</button>', research_content[btn_match.start():])
    if btn_end_match:
        btn_full = research_content[btn_match.start():btn_match.start() + btn_end_match.end()]
        print(f"\n按钮完整内容前100字: {btn_full[:100]}...")
        
        # 替换按钮
        # 保留按钮里的图标和文字
        inner_match = re.search(r'<button[^>]*>(.*?)</button>', btn_full, re.DOTALL)
        if inner_match:
            inner = inner_match.group(1)
            new_btn_full = new_btn + inner + '</button>'
            research_content = research_content.replace(btn_full, new_btn_full)
            print("\n✅ 客户背调生成按钮已改成白色样式")

# 3. 找方案生成按钮
solution_start = content.find("id=\"solution\"")
solution_end = content.find("</section>", solution_start)
solution_content = content[solution_start:solution_end]

btn_match2 = re.search(r'<button[^>]*generateSolution[^>]*>', solution_content)
if btn_match2:
    print(f"\n方案生成按钮实际样式：")
    print(f"  {btn_match2.group()[:150]}...")

# 替换回去
content = content[:research_start] + research_content + content[research_end:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("\n✅ 已修复下拉框文字bug")
