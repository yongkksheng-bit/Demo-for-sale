with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 把 smooth 滚动改成直接滚动
content = content.replace(
    "window.scrollTo({ top: 0, behavior: 'smooth' });",
    "window.scrollTo(0, 0);"
)

# 保存
with open("app.js", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ 已把滚动改成直接滚动，更可靠")
