with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找"销售话术生成"，看看右侧内容的标题大小
idx = content.find("销售话术生成")
if idx != -1:
    print("=== 销售话术生成附近 ===")
    print(content[idx-200:idx+200])
