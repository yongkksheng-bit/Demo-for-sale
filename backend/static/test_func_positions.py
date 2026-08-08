with open("app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找到所有身份相关函数的位置
functions = [
    "showIdentityModal",
    "hideIdentityModal",
    "selectIndustry",
    "selectSalesType", 
    "updateIdentitySelectionUI",
    "confirmIdentity",
    "updateIdentityDisplay",
    "loadIdentity"
]

print("=== 身份相关函数位置 ===\n")

for func in functions:
    found = False
    for i, line in enumerate(lines):
        if f"function {func}" in line:
            print(f"✅ {func}: 第 {i+1} 行")
            found = True
            break
    if not found:
        print(f"❌ {func}: 未找到")

# 检查变量声明
print("\n=== 变量声明 ===\n")
for i, line in enumerate(lines):
    if "identityIndustry" in line and ("let " in line or "var " in line or "const " in line):
        print(f"identityIndustry: 第 {i+1} 行 - {line.strip()}")
    if "identitySalesType" in line and ("let " in line or "var " in line or "const " in line):
        print(f"identitySalesType: 第 {i+1} 行 - {line.strip()}")
    if "currentIdentity" in line and ("let " in line or "var " in line or "const " in line):
        print(f"currentIdentity: 第 {i+1} 行 - {line.strip()}")
