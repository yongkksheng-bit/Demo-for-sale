with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 找 showSection 函数
start = content.find("function showSection")
end = content.find("}", start) + 1
func = content[start:end]
print("=== showSection 函数 ===")
print(func)
