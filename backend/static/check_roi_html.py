with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找到ROI计算器的输入框
roi_start = content.find("ROI 投资回报计算器")
roi_end = content.find("</div>", content.find("tool-content-roi", roi_start) + 500)
roi_content = content[roi_start:roi_end]

print("=== ROI计算器输入框 ===")
import re
inputs = re.findall(r'<input[^>]*id="([^"]+)"[^>]*>', roi_content)
for inp in inputs:
    idx = roi_content.find(f'id="{inp}"')
    tag_start = roi_content.rfind("<input", 0, idx)
    tag_end = roi_content.find(">", idx) + 1
    tag = roi_content[tag_start:tag_end]
    has_oninput = "oninput" in tag
    print(f"  id: {inp}, oninput: {'✅' if has_oninput else '❌'}")

# 检查结果显示的id
print("\n=== ROI结果显示id ===")
results = re.findall(r'id="(roi-[^"]+)"', roi_content)
for r in results:
    print(f"  {r}")
