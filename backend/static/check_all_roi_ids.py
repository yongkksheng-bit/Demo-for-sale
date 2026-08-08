with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找所有roi相关的id
import re
all_roi_ids = re.findall(r'id="(roi-[^"]+)"', content)
print("=== 所有roi相关的id ===")
for rid in all_roi_ids:
    print(f"  {rid}")

# 检查 roi-cost 输入框有没有 oninput
roi_cost_idx = content.find('id="roi-cost"')
if roi_cost_idx != -1:
    tag_start = content.rfind("<input", 0, roi_cost_idx)
    tag_end = content.find(">", roi_cost_idx) + 1
    tag = content[tag_start:tag_end]
    print(f"\n=== roi-cost 输入框 ===")
    print(tag)
    print(f"oninput: {'✅' if 'oninput' in tag else '❌'}")
