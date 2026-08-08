with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

# 检查各个接口是否都有 identity 参数
endpoints = [
    ("/solution/generate", "方案生成"),
    ("/solution/generate-stream", "方案生成流式"),
    ("/chat", "对话"),
    ("/chat/stream", "对话流式"),
    ("/company-research", "客户背调"),
    ("/sales-script", "销售话术"),
    ("/sales-script/stream", "销售话术流式"),
    ("/objection", "异议处理"),
    ("/objection/stream", "异议处理流式"),
    ("/competitor-compare", "竞品对比"),
    ("/competitor-compare/stream", "竞品对比流式"),
    ("/visit-checklist", "拜访清单"),
    ("/visit-checklist/stream", "拜访清单流式"),
    ("/bid/analyze", "招标文件分析"),
]

print("=== 后端接口 identity 参数检查 ===\n")

all_ok = True
for endpoint, display_name in endpoints:
    # 找到这个接口的定义
    idx = content.find(endpoint)
    if idx == -1:
        print(f"⚠️  {display_name}: 接口不存在")
        continue
    
    # 看看函数定义里有没有 identity
    # 找到函数定义的开始
    def_idx = content.find("def ", idx - 100)
    if def_idx == -1:
        print(f"⚠️  {display_name}: 找不到函数定义")
        continue
    
    # 找到函数参数的结束
    param_end = content.find("):", def_idx)
    if param_end == -1:
        print(f"⚠️  {display_name}: 找不到参数结束")
        continue
    
    params = content[def_idx:param_end]
    has_identity = "identity" in params
    status = "✅" if has_identity else "❌"
    print(f"{status} {display_name}: identity={'有' if has_identity else '没有'}")
    if not has_identity:
        all_ok = False

print(f"\n{'全部接口都有identity参数！' if all_ok else '还有接口没有identity参数！'}")
