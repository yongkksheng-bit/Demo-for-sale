with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 检查 DOMContentLoaded 里有没有 calculateROI
if "DOMContentLoaded" in content:
    # 找到所有 DOMContentLoaded 事件
    import re
    matches = re.findall(r'DOMContentLoaded[^}]*}', content, re.DOTALL)
    for i, match in enumerate(matches):
        print(f"=== DOMContentLoaded 事件 {i+1} ===")
        if "calculateROI" in match:
            print("✅ 包含 calculateROI")
        else:
            print("❌ 不包含 calculateROI")
else:
    print("❌ 找不到 DOMContentLoaded 事件")

# 检查 selectTool 里有没有调用 calculateROI
if "selectTool" in content:
    start = content.find("function selectTool")
    end = content.find("}", start) + 1
    func = content[start:end]
    if "calculateROI" in func:
        print("\n✅ selectTool 里调用了 calculateROI")
    else:
        print("\n❌ selectTool 里没调用 calculateROI")
