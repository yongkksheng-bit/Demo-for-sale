with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找客户背调区域
research_start = content.find("客户背调")
research_end = content.find('</section>', research_start)
research_content = content[research_start:research_end]

import re
buttons = re.findall(r'<button[^>]*>(.*?)</button>', research_content, re.DOTALL)
print(f"客户背调按钮数量: {len(buttons)}")
for i, btn in enumerate(buttons[:5]):
    print(f"\n按钮 {i+1}: {btn.strip()[:50]}...")
    # 找class
    btn_tag_match = re.search(r'<button[^>]*class="([^"]*)"[^>]*>', research_content[research_content.find(btn)-200:research_content.find(btn)+len(btn)])
    if btn_tag_match:
        print(f"  class: {btn_tag_match.group(1)[:80]}...")
