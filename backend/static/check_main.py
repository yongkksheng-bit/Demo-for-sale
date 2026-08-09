with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找 main 开始
main_start = None
for i, line in enumerate(lines):
    if '<main' in line:
        main_start = i
        break

# 找 main 结束
main_end = None
for i in range(len(lines)-1, -1, -1):
    if '</main>' in lines[i]:
        main_end = i
        break

print(f"main 元素: 第 {main_start+1} 行 开始, 第 {main_end+1} 行 结束")
print(f"共 {main_end - main_start + 1} 行")

# 检查 main 里面有多少个 section
main_content = ''.join(lines[main_start:main_end+1])
section_start = main_content.count('<section')
section_end = main_content.count('</section>')
print(f"main 里面的 section: {section_start} 开始 / {section_end} 结束")

# 检查销售工具箱是不是在 main 里面
tools_line = None
for i, line in enumerate(lines):
    if 'id="tools"' in line:
        tools_line = i
        break

print(f"\n销售工具箱在第 {tools_line+1} 行")
if main_start < tools_line < main_end:
    print("✅ 销售工具箱在 main 里面（正确）")
else:
    print("❌ 销售工具箱不在 main 里面（有问题）")
