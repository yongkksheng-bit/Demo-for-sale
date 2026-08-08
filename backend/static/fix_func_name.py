with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 把身份选择的 selectIndustry 改成 selectIdentityIndustry
# 先找到身份选择的那个函数定义，替换函数名
old_func = "function selectIndustry(industry) {\n    identityIndustry = industry;\n    updateIdentitySelectionUI();"
new_func = "function selectIdentityIndustry(industry) {\n    identityIndustry = industry;\n    updateIdentitySelectionUI();"

if old_func in content:
    content = content.replace(old_func, new_func)
    print("✅ 函数名已改为 selectIdentityIndustry")
else:
    print("❌ 找不到函数")

with open("app.js", "w", encoding="utf-8") as f:
    f.write(content)
