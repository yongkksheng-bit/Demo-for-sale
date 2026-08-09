with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找三步上手
idx = content.find("三步上手")
if idx != -1:
    print("=== 三步上手附近 ===")
    print(content[idx-100:idx+800])
