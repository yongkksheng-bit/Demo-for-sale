with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找到 tool-content-roi
roi_start = content.find('id="tool-content-roi"')
if roi_start == -1:
    print("❌ 找不到 tool-content-roi")
else:
    # 找到这个div的结束
    # 简单点，找后面的第一个 </div> 不对，应该找匹配的
    # 先找后面1000个字符
    roi_content = content[roi_start:roi_start + 2000]
    
    import re
    inputs = re.findall(r'<input[^>]*id="([^"]+)"[^>]*>', roi_content)
    print("=== ROI输入框 ===")
    for inp in inputs:
        idx = roi_content.find(f'id="{inp}"')
        tag_start = roi_content.rfind("<input", 0, idx)
        tag_end = roi_content.find(">", idx) + 1
        tag = roi_content[tag_start:tag_end]
        has_oninput = "oninput" in tag
        print(f"  id: {inp}, oninput: {'✅' if has_oninput else '❌'}")
    
    # 结果显示的id
    results = re.findall(r'id="(roi-[^"]+)"', roi_content)
    print("\n=== 结果显示id ===")
    for r in results:
        print(f"  {r}")
