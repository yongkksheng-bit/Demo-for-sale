with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找侧边栏底部的身份切换区域
idx = content.find("点击切换身份")
if idx != -1:
    # 往前找
    start = content.rfind("<div", 0, idx - 200)
    print("=== 身份切换区域 ===")
    print(content[start:start+500])
