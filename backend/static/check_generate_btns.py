with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re

# 找"生成"相关的按钮
generate_btns = re.findall(r'<button[^>]*>[^<]*生成[^<]*</button>', content)
print(f"生成按钮数量: {len(generate_btns)}")
for i, btn in enumerate(generate_btns[:10]):
    print(f"\n按钮 {i+1}:")
    print(f"  {btn[:100]}...")
