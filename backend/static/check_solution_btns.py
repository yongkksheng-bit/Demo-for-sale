with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找方案生成区域的行业按钮
solution_start = content.find('id="solution"')
if solution_start != -1:
    solution_end = content.find('</section>', solution_start)
    solution_content = content[solution_start:solution_end]
    
    # 看看里面的行业按钮
    import re
    buttons = re.findall(r'<button[^>]*class="[^"]*industry[^"]*"[^>]*>', solution_content)
    print(f"方案生成区域行业按钮数量: {len(buttons)}")
    if buttons:
        print(f"第一个按钮: {buttons[0][:200]}")
    
    # 看看有没有 onclick
    has_onclick = "onclick=" in solution_content
    print(f"方案生成区域有 onclick: {has_onclick}")
