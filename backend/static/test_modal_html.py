with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找到模态框的开始
idx = content.find('id="identity-modal"')
if idx != -1:
    # 往前找标签开始
    tag_start = content.rfind("<", 0, idx)
    # 往后找标签结束
    tag_end = content.find(">", idx) + 1
    print("=== 模态框开始标签 ===")
    print(content[tag_start:tag_end])
    
    # 看看有没有 hidden 类
    has_hidden = "hidden" in content[tag_start:tag_end]
    print(f"\n默认隐藏: {has_hidden}")
    
    # 看看模态框的结构
    print("\n=== 模态框前10行 ===")
    lines = content[idx-50:idx+500].split("\n")
    for i, line in enumerate(lines[:15]):
        print(f"{i+1}: {line.strip()}")
else:
    print("❌ 找不到 identity-modal")
