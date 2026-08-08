with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re

# 找客户管理区域
customers_start = content.find("id=\"customers\"")
if customers_start == -1:
    customers_start = content.find("客户管理")
customers_end = content.find("</section>", customers_start)
customers_content = content[customers_start:customers_end]

# 找客户卡片
customer_cards = re.findall(r'class="[^"]*bg[^"]*rounded[^"]*p[^"]*"', customers_content)
print(f"客户管理卡片数量: {len(customer_cards)}")
for i, card in enumerate(customer_cards[:5]):
    print(f"\n卡片 {i+1}: {card[:80]}...")

# 找按钮
customer_btns = re.findall(r'<button[^>]*class="([^"]*)"[^>]*>', customers_content)
print(f"\n客户管理按钮数量: {len(customer_btns)}")
for i, btn in enumerate(customer_btns[:5]):
    print(f"\n按钮 {i+1}: {btn[:80]}...")
    
# 找黑色背景按钮
black_btns = [b for b in customer_btns if 'bg-gray-900' in b or 'bg-gradient' in b]
print(f"\n黑色背景按钮数量: {len(black_btns)}")
for i, btn in enumerate(black_btns[:3]):
    print(f"  {btn[:80]}...")
