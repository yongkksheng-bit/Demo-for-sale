with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找 id="chat" 的标签
idx = content.find('id="chat"')
if idx != -1:
    # 往前找标签开始
    tag_start = content.rfind("<", 0, idx)
    tag_end = content.find(">", idx) + 1
    tag = content[tag_start:tag_end]
    print(f"id=\"chat\" 的标签: {tag[:100]}")
    
    # 看看是 section 还是 div
    if tag.startswith("<section"):
        print("是 section 标签")
    elif tag.startswith("<div"):
        print("是 div 标签")
