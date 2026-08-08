with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 修复每个函数的最后一个参数后面没有逗号的问题
# 找到 "scenario: scenario\n                identity" 改成 "scenario: scenario,\n                identity"
content = content.replace(
    "scenario: scenario\n                identity: currentIdentity,",
    "scenario: scenario,\n                identity: currentIdentity,"
)

# 找到 "industry: industry\n                identity" 改成 "industry: industry,\n                identity"
content = content.replace(
    "industry: industry\n                identity: currentIdentity,",
    "industry: industry,\n                identity: currentIdentity,"
)

# 找到 "position: position\n                identity" 改成 "position: position,\n                identity"
content = content.replace(
    "position: position\n                identity: currentIdentity,",
    "position: position,\n                identity: currentIdentity,"
)

with open("app.js", "w", encoding="utf-8") as f:
    f.write(content)

print("逗号问题修复完成！")
