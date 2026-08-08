with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 检查 showIdentityModal 出现的次数
count = content.count("showIdentityModal")
print(f"showIdentityModal 出现次数: {count}")

# 检查所有函数声明
import re
func_declarations = re.findall(r'function\s+(\w+)\s*\(', content)
print(f"\n总函数数量: {len(func_declarations)}")

# 检查有没有重名的函数
from collections import Counter
func_counts = Counter(func_declarations)
duplicates = {k: v for k, v in func_counts.items() if v > 1}
if duplicates:
    print(f"\n❌ 重名函数: {duplicates}")
else:
    print("\n✅ 没有重名函数")

# 检查身份相关的函数有没有重名
identity_funcs = ["showIdentityModal", "hideIdentityModal", "selectIndustry", "selectSalesType", 
                  "updateIdentitySelectionUI", "confirmIdentity", "updateIdentityDisplay", "loadIdentity"]
print("\n=== 身份相关函数检查 ===")
for func in identity_funcs:
    count = func_counts.get(func, 0)
    status = "✅" if count == 1 else "❌"
    print(f"{status} {func}: {count} 次")
