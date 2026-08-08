with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

import re
from collections import Counter

# 检查所有函数声明
func_declarations = re.findall(r'function\s+(\w+)\s*\(', content)
func_counts = Counter(func_declarations)
duplicates = {k: v for k, v in func_counts.items() if v > 1}

if duplicates:
    print(f"❌ 还有重名函数: {duplicates}")
else:
    print("✅ 没有重名函数了")

# 再检查一下身份相关的函数
identity_funcs = ["showIdentityModal", "hideIdentityModal", "selectIdentityIndustry", "selectSalesType", 
                  "updateIdentitySelectionUI", "confirmIdentity", "updateIdentityDisplay", "loadIdentity"]
print("\n=== 身份相关函数 ===")
for func in identity_funcs:
    count = func_counts.get(func, 0)
    status = "✅" if count == 1 else "❌"
    print(f"{status} {func}: {count} 次")
