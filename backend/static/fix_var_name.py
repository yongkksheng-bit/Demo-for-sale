with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 把身份选择的变量改名，避免和方案生成的变量重名
# 方案生成的是 selectedIndustry（第9行）
# 身份选择的改成 identityIndustry 和 identitySalesType

# 先找到身份选择部分的变量声明
old_declare = """let selectedIndustry = "";
let selectedSalesType = "";"""

new_declare = """let identityIndustry = "";
let identitySalesType = "";"""

content = content.replace(old_declare, new_declare, 1)  # 只替换第一个（身份选择部分的）

# 然后替换身份选择函数里的变量引用
# 注意：只替换身份选择部分的，不要替换方案生成部分的

# 找到身份选择部分的开始和结束
start_marker = "// ========== 身份选择 =========="
end_marker = "// ========== 页面切换 =========="  # 不对，页面切换在身份选择前面？

# 换个方式：找到 updateIdentitySelectionUI 函数的开始和结束
# 或者直接替换 showIdentityModal 到 loadIdentity 之间的内容

# 简单点，直接把身份选择部分的 selectedIndustry 替换成 identityIndustry
# 但是要小心不要替换到方案生成的部分

# 找到身份选择部分的范围
start_idx = content.find(start_marker)
# 找到 loadIdentity 函数结束的位置
load_identity_idx = content.find("function loadIdentity", start_idx)
end_idx = content.find("\n}\n", load_identity_idx) + 3

if start_idx != -1 and end_idx != -1:
    identity_section = content[start_idx:end_idx]
    # 替换变量名
    identity_section = identity_section.replace("selectedIndustry", "identityIndustry")
    identity_section = identity_section.replace("selectedSalesType", "identitySalesType")
    # 替换回去
    content = content[:start_idx] + identity_section + content[end_idx:]
    
    with open("app.js", "w", encoding="utf-8") as f:
        f.write(content)
    print("变量名修改完成！")
else:
    print(f"找不到范围: start={start_idx}, end={end_idx}")
