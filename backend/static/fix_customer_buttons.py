with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re

# 找客户管理区域
customers_start = content.find("id=\"customers\"")
if customers_start == -1:
    customers_start = content.find("客户管理")
customers_end = content.find("</section>", customers_start)
customers_content = content[customers_start:customers_end]

# 找所有渐变按钮
gradient_btns = re.findall(r'<button[^>]*bg-gradient-primary[^>]*>.*?</button>', customers_content, re.DOTALL)
print(f"找到 {len(gradient_btns)} 个渐变按钮")

for i, btn in enumerate(gradient_btns):
    # 提取按钮内容
    inner_match = re.search(r'<button[^>]*>(.*?)</button>', btn, re.DOTALL)
    if inner_match:
        inner = inner_match.group(1)
        
        # 提取 onclick
        onclick_match = re.search(r'onclick="([^"]*)"', btn)
        onclick = onclick_match.group(0) if onclick_match else ''
        
        # 提取 id
        id_match = re.search(r'id="([^"]*)"', btn)
        id_attr = id_match.group(0) if id_match else ''
        
        # 判断按钮大小
        if 'py-3' in btn:
            # 大按钮
            new_btn = f'<button {onclick} {id_attr} class="px-6 py-3 bg-white border border-gray-200 text-gray-900 rounded-xl hover:bg-gray-50 hover:shadow-md transition-all font-semibold shadow-sm">{inner}</button>'
        else:
            # 小按钮
            new_btn = f'<button {onclick} {id_attr} class="px-4 py-2 bg-white border border-gray-200 text-gray-900 rounded-lg hover:bg-gray-50 hover:shadow-md transition-all text-sm font-medium shadow-sm">{inner}</button>'
        
        customers_content = customers_content.replace(btn, new_btn)
        print(f"✅ 已修改第 {i+1} 个按钮")

# 替换回去
content = content[:customers_start] + customers_content + content[customers_end:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("\n✅ 客户管理页面的渐变按钮已改成白色样式")
