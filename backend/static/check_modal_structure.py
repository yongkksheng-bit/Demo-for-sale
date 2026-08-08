with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找到模态框的结构
modal_start = content.find('id="identity-modal"')
modal_end = content.find('</div>\n    </div>\n</div>', modal_start) + len('</div>\n    </div>\n</div>')

modal_content = content[modal_start:modal_end]
print("=== 当前模态框结构（前30行）===")
lines = modal_content.split("\n")
for i, line in enumerate(lines[:30]):
    print(f"{i+1}: {line.strip()}")
