with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 找到 calculateROI 函数
start = content.find("function calculateROI")
if start == -1:
    print("❌ 找不到 calculateROI 函数")
else:
    end = content.find("\nfunction ", start + 1)
    if end == -1:
        end = len(content)
    
    func_content = content[start:end]
    print("=== calculateROI 函数 ===")
    print(func_content)
    
    # 检查用到的元素 id
    import re
    ids = re.findall(r'getElementById\(["\']([^"\']+)["\']\)', func_content)
    print(f"\n用到的元素 id: {ids}")
