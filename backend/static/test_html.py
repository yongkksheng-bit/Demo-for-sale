with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 检查1：模态框是否存在
has_modal = "identity-modal" in content
print(f"✅ 模态框存在: {has_modal}")

# 检查2：行业选项数量
industry_count = content.count("selectIndustry(")
print(f"✅ 行业选项数量: {industry_count} 个（应该是8个）")

# 检查3：销售类型选项数量
sales_type_count = content.count("selectSalesType(")
print(f"✅ 销售类型选项数量: {sales_type_count} 个（应该是4个）")

# 检查4：确认按钮是否存在
has_confirm_btn = "confirm-identity-btn" in content
print(f"✅ 确认按钮存在: {has_confirm_btn}")

# 检查5：首页身份按钮id
has_hero_identity = "hero-identity-text" in content
print(f"✅ 首页身份按钮id存在: {has_hero_identity}")

# 检查6：侧边栏身份显示id
has_sidebar_identity = "current-identity-name" in content
print(f"✅ 侧边栏身份显示id存在: {has_sidebar_identity}")

# 检查7：第二步销售类型区域是否有id
has_sales_type_section = "sales-type-section" in content
print(f"✅ 销售类型区域id存在: {has_sales_type_section}")

# 检查8：第二步徽章是否有id
has_step2_badge = "step2-badge" in content
print(f"✅ 第二步徽章id存在: {has_step2_badge}")
