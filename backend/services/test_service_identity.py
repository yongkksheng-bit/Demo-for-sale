with open("solution_service.py", "r", encoding="utf-8") as f:
    content = f.read()

# 检查各个函数的参数里有没有 identity
functions = [
    ("def generate_solution", "生成方案"),
    ("def generate_solution_stream", "生成方案流式"),
    ("def generate_company_research", "客户背调"),
    ("def generate_sales_script", "销售话术"),
    ("def generate_sales_script_stream", "销售话术流式"),
    ("def handle_objection", "异议处理"),
    ("def handle_objection_stream", "异议处理流式"),
    ("def compare_competitor", "竞品对比"),
    ("def compare_competitor_stream", "竞品对比流式"),
    ("def generate_visit_checklist", "拜访清单"),
    ("def generate_visit_checklist_stream", "拜访清单流式"),
]

print("=== 服务层函数 identity 参数检查 ===\n")

all_ok = True
for func_name, display_name in functions:
    idx = content.find(func_name)
    if idx == -1:
        print(f"⚠️  {display_name}: 函数不存在")
        all_ok = False
        continue
    
    # 找到函数参数的结束
    param_end = content.find("):", idx)
    if param_end == -1:
        print(f"⚠️  {display_name}: 找不到参数结束")
        all_ok = False
        continue
    
    params = content[idx:param_end]
    has_identity = "identity" in params
    status = "✅" if has_identity else "❌"
    print(f"{status} {display_name}: identity={'有' if has_identity else '没有'}")
    if not has_identity:
        all_ok = False

print(f"\n{'所有函数都有identity参数！' if all_ok else '还有函数没有identity参数！'}")
