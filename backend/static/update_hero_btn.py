with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找到首页选择身份按钮的span，加上id
old_text = "<span>选择身份</span>"
new_text = '<span id="hero-identity-text">选择身份</span>'

# 只替换第一个（首页的那个）
content = content.replace(old_text, new_text, 1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("首页身份按钮id添加完成！")
