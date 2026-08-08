with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

import re
from collections import Counter

# 检查所有函数声明
func_declarations = re.findall(r'function\s+(\w+)\s*\(', content)
func_counts = Counter(func_declarations)
duplicates = {k: v for k, v in func_counts.items() if v > 1}

if duplicates:
    print(f"❌ 重名函数: {duplicates}")
else:
    print("✅ 没有重名函数")

# 检查 selectTool 函数
print(f"\nselectTool 函数声明次数: {func_counts.get('selectTool', 0)}")

# 检查销售工具箱相关的函数
tool_funcs = ["generateSalesScript", "handleObjection", "generateCompetitorCompare", "generateVisitChecklist", "calculateROI", "setObjection"]
print("\n=== 销售工具箱相关函数 ===")
for func in tool_funcs:
    count = func_counts.get(func, 0)
    status = "✅" if count == 1 else "❌"
    print(f"{status} {func}: {count} 次")
