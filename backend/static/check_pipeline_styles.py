with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re

# 找销售看板区域
pipeline_start = content.find("id=\"pipeline\"")
if pipeline_start == -1:
    pipeline_start = content.find("销售看板")
pipeline_end = content.find("</section>", pipeline_start)
pipeline_content = content[pipeline_start:pipeline_end]

# 找统计卡片
stat_cards = re.findall(r'class="[^"]*bg[^"]*rounded[^"]*p[^"]*"', pipeline_content)
print(f"销售看板统计卡片数量: {len(stat_cards)}")
for i, card in enumerate(stat_cards[:4]):
    print(f"\n卡片 {i+1}: {card[:80]}...")

# 找按钮
pipeline_btns = re.findall(r'<button[^>]*class="([^"]*)"[^>]*>', pipeline_content)
print(f"\n销售看板按钮数量: {len(pipeline_btns)}")
for i, btn in enumerate(pipeline_btns[:3]):
    print(f"\n按钮 {i+1}: {btn[:80]}...")
