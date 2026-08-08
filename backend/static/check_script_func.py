with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 找到 generateSalesScript 函数
start = content.find("function generateSalesScript")
end = content.find("\nfunction ", start + 1)
if end == -1:
    end = len(content)

func_content = content[start:end]
print("=== generateSalesScript 函数 ===")
print(func_content[:500])

# 提取里面用到的 getElementById 的 id
import re
ids = re.findall(r'getElementById\(["\']([^"\']+)["\']\)', func_content)
print(f"\n用到的元素 id: {ids}")
