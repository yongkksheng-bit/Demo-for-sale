with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re

# 找所有bg-gray-900的按钮（黑色背景按钮）
black_buttons = re.findall(r'<button[^>]*bg-gray-900[^>]*>', content)
print(f"黑色背景按钮数量: {len(black_buttons)}")

# 看看主要功能区域的按钮
areas = ["客户背调", "方案生成", "销售看板", "客户管理", "智能对话"]
for area in areas:
    idx = content.find(area)
    if idx != -1:
        # 找附近的按钮
        search_area = content[idx:idx + 3000]
        buttons = re.findall(r'<button[^>]*class="([^"]*)"[^>]*>', search_area)
        black_count = sum(1 for b in buttons if 'bg-gray-900' in b)
        white_count = sum(1 for b in buttons if 'bg-white' in b)
        print(f"\n{area}: 黑色按钮 {black_count} 个, 白色按钮 {white_count} 个")
