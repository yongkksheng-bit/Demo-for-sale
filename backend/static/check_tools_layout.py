with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找到销售工具箱区域
tools_start = content.find('id="tools"')
if tools_start == -1:
    tools_start = content.find('销售工具箱')

if tools_start != -1:
    # 找到下一个section或者下一个大的div
    tools_end = content.find('</section>', tools_start)
    if tools_end == -1:
        tools_end = content.find('id="', tools_start + 10)
    
    tools_content = content[tools_start:tools_end]
    lines = tools_content.split("\n")
    print(f"=== 销售工具箱区域（前50行）===")
    for i, line in enumerate(lines[:50]):
        print(f"{i+1}: {line.strip()}")
