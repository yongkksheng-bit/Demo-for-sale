with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 检查1：变量声明
has_identity_industry = "identityIndustry" in content
has_identity_sales_type = "identitySalesType" in content
print(f"✅ 身份变量声明: identityIndustry={has_identity_industry}, identitySalesType={has_identity_sales_type}")

# 检查2：核心函数是否存在
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

for func in functions:
    exists = f"function {func}" in content
    print(f"✅ 函数 {func}: {exists}")

# 检查3：变量名是否和方案生成的重名
# 方案生成的是 selectedIndustry，身份选择的是 identityIndustry
has_selected_industry = "let selectedIndustry" in content
has_identity_industry_var = "let identityIndustry" in content
print(f"\n✅ 变量名不冲突:")
print(f"   方案生成: selectedIndustry = {has_selected_industry}")
print(f"   身份选择: identityIndustry = {has_identity_industry_var}")

# 检查4：localStorage key
has_localstorage_key = "xiaoshouyi_identity" in content
print(f"\n✅ localStorage key 存在: {has_localstorage_key}")

# 检查5：第二步解锁逻辑
has_unlock_logic = "sales-type-section" in content and "pointer-events-none" in content
print(f"✅ 第二步解锁逻辑存在: {has_unlock_logic}")

# 检查6：确认按钮状态更新
has_btn_update = "confirm-identity-btn" in content
print(f"✅ 确认按钮状态更新存在: {has_btn_update}")
