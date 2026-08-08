with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 检查1：首页"选择身份"按钮
print("=== 首页身份按钮 ===")
idx = content.find("hero-identity-text")
if idx != -1:
    # 往前找按钮
    btn_start = content.rfind("<button", 0, idx)
    btn_end = content.find("</button>", idx) + len("</button>")
    print(content[btn_start:btn_end])
else:
    print("❌ 找不到 hero-identity-text")

print("\n=== 侧边栏身份区域 ===")
idx = content.find("current-identity-name")
if idx != -1:
    # 往前找点击区域
    click_start = content.rfind("onclick=", 0, idx)
    if click_start != -1:
        click_end = content.find(")", click_start) + 1
        print(f"点击事件: {content[click_start:click_end]}")
    else:
        print("❌ 找不到点击事件")
else:
    print("❌ 找不到 current-identity-name")

print("\n=== 模态框 ===")
has_modal = "identity-modal" in content
print(f"模态框存在: {has_modal}")

# 检查模态框的关闭按钮
if has_modal:
    has_close_btn = "hideIdentityModal" in content
    print(f"关闭按钮事件: {has_close_btn}")

print("\n=== 行业按钮 ===")
industry_btns = content.count("selectIndustry(")
print(f"行业按钮数量: {industry_btns}")

print("\n=== 销售类型按钮 ===")
sales_type_btns = content.count("selectSalesType(")
print(f"销售类型按钮数量: {sales_type_btns}")

print("\n=== 确认按钮 ===")
has_confirm_btn = "confirmIdentity()" in content
print(f"确认按钮事件: {has_confirm_btn}")
