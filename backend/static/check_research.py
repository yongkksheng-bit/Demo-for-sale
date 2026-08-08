with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 1. 修复客户背调 - generateResearch 函数
# 先看看这个函数里的 fetch 请求
idx = content.find("function generateResearch")
if idx != -1:
    end_idx = content.find("\n}", idx) + 2
    func_content = content[idx:end_idx]
    print("=== 客户背调函数 ===")
    print(func_content[:500])
    print("...")
