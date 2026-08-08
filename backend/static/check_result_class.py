with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 方案生成结果区域
idx = content.find('id="solution-content"')
if idx != -1:
    tag_start = content.rfind("<", 0, idx)
    tag_end = content.find(">", idx) + 1
    tag = content[tag_start:tag_end]
    print(f"方案生成结果区域: {tag[:120]}...")

# 客户背调结果区域
idx = content.find('id="research-result"')
if idx != -1:
    tag_start = content.rfind("<", 0, idx)
    tag_end = content.find(">", idx) + 1
    tag = content[tag_start:tag_end]
    print(f"\n客户背调结果区域: {tag[:120]}...")
