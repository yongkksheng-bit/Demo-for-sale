with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

functions_to_check = [
    ("generateSalesScript", "销售话术"),
    ("handleObjection", "异议处理"), 
    ("generateCompetitorCompare", "竞品对比"),
    ("generateVisitChecklist", "拜访清单"),
    ("generateResearch", "客户背调"),
    ("generateSolution", "方案生成"),
    ("sendMessage", "智能对话"),
    ("handleBidFileUpload", "招标文件分析"),
]

print("=== 所有功能 identity 参数检查 ===\n")

all_ok = True
for func_name, display_name in functions_to_check:
    search_str = f"async function {func_name}"
    if search_str not in content:
        search_str = f"function {func_name}"
    
    idx = content.find(search_str)
    if idx == -1:
        print(f"❌ {display_name}: 函数不存在")
        all_ok = False
        continue
    
    # 找 fetch 请求
    fetch_idx = content.find("fetch(", idx)
    if fetch_idx == -1:
        # 可能是流式的，找 EventSource 或者其他
        if "EventSource" in content[idx:idx+1000] or "ReadableStream" in content[idx:idx+1000]:
            # 再检查一下 body 里有没有 identity
            body_start = content.find("body:", idx)
            if body_start != -1 and body_start < idx + 1000:
                body_end = content.find("})", body_start)
                body_content = content[body_start:body_end]
                has_identity = "identity" in body_content
                status = "✅" if has_identity else "❌"
                print(f"{status} {display_name}: identity={'有' if has_identity else '没有'}")
                if not has_identity:
                    all_ok = False
                continue
        print(f"⚠️  {display_name}: 没有fetch请求")
        continue
    
    body_start = content.find("body: JSON.stringify({", fetch_idx)
    if body_start == -1:
        # 可能是 FormData
        if "FormData" in content[idx:idx+1000]:
            formdata_idx = content.find("FormData", idx)
            append_count = content.count(".append(", formdata_idx, formdata_idx + 500)
            has_identity_append = "identity" in content[formdata_idx:formdata_idx+500]
            status = "✅" if has_identity_append else "❌"
            print(f"{status} {display_name}: identity={'有' if has_identity_append else '没有'} (FormData)")
            if not has_identity_append:
                all_ok = False
            continue
        print(f"⚠️  {display_name}: 没有JSON请求体")
        continue
    
    body_end = content.find("})", body_start)
    body_content = content[body_start:body_end]
    
    has_identity = "identity" in body_content
    status = "✅" if has_identity else "❌"
    print(f"{status} {display_name}: identity={'有' if has_identity else '没有'}")
    if not has_identity:
        all_ok = False

print(f"\n{'全部通过！' if all_ok else '还有问题！'}")
