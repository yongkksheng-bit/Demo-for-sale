with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 找 showSection 函数
idx = content.find("function showSection")
if idx != -1:
    # 找到函数结束位置
    end_idx = content.find("\n}", idx) + 2
    old_func = content[idx:end_idx]
    print("=== 旧的 showSection 函数 ===")
    print(old_func[:300])
    
    # 在函数开头加上 window.scrollTo(0, 0)
    new_func = old_func.replace(
        "function showSection(sectionId) {",
        "function showSection(sectionId) {\n    // 滚动到顶部\n    window.scrollTo(0, 0);"
    )
    
    content = content[:idx] + new_func + content[end_idx:]
    
    # 保存
    with open("app.js", "w", encoding="utf-8") as f:
        f.write(content)
    
    print("\n✅ 已添加滚动到顶部")
else:
    print("❌ 没找到 showSection 函数")
