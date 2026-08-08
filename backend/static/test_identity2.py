with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 检查各个函数的请求体里有没有identity
functions_to_check = [
    ("generateSalesScript", "销售话术"),
    ("handleObjection", "异议处理"), 
    ("generateCompetitorCompare", "竞品对比"),
    ("generateVisitChecklist", "拜访清单"),
]

for func_name, display_name in functions_to_check:
    # 找到函数定义
    search_str = f"async function {func_name}"
    if search_str not in content:
        search_str = f"function {func_name}"
    
    idx = content.find(search_str)
    if idx == -1:
        print(f"❌ {display_name}: 函数不存在")
        continue
    
    # 找到函数里的 fetch 请求
    fetch_idx = content.find("fetch(", idx)
    if fetch_idx == -1:
        print(f"⚠️  {display_name}: 没有fetch请求")
        continue
    
    # 找到 body: JSON.stringify({ 那一段
    body_start = content.find("body: JSON.stringify({", fetch_idx)
    if body_start == -1:
        print(f"⚠️  {display_name}: 没有JSON请求体")
        continue
    
    # 找到请求体的结束 })
    body_end = content.find("})", body_start)
    body_content = content[body_start:body_end]
    
    has_identity = "identity" in body_content
    status = "✅" if has_identity else "❌"
    print(f"{status} {display_name}: identity={'有' if has_identity else '没有'}")
    
    if not has_identity:
        # 打印请求体内容，方便调试
        print(f"   请求体: {body_content[:200]}...")
