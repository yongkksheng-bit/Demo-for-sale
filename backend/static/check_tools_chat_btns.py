with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re

# 检查智能对话发送按钮
chat_start = content.find("id=\"chat\"")
chat_end = content.find("</section>", chat_start)
chat_content = content[chat_start:chat_end]

send_btn = re.search(r'<button[^>]*sendMessage[^>]*>.*?</button>', chat_content, re.DOTALL)
if send_btn:
    print("=== 智能对话发送按钮 ===")
    print(send_btn.group()[:200])
    if 'onclick' in send_btn.group():
        print("✅ 有onclick")
    else:
        print("❌ 没有onclick！")

# 检查销售工具箱的按钮
tools_start = content.find("id=\"tools\"")
if tools_start == -1:
    tools_start = content.find("销售工具箱")
tools_end = content.find("</section>", tools_start)
tools_content = content[tools_start:tools_end]

# 检查生成话术按钮
script_btn = re.search(r'<button[^>]*generateSalesScript[^>]*>.*?</button>', tools_content, re.DOTALL)
if script_btn:
    print("\n=== 销售话术生成按钮 ===")
    print(script_btn.group()[:200])
    if 'onclick' in script_btn.group():
        print("✅ 有onclick")
    else:
        print("❌ 没有onclick！")

# 检查左侧工具导航按钮
nav_btns = re.findall(r'<button[^>]*tool-nav-btn[^>]*>', tools_content)
print(f"\n销售工具箱左侧导航按钮数量: {len(nav_btns)}")
for i, btn in enumerate(nav_btns[:2]):
    print(f"\n导航按钮 {i+1}: {btn[:100]}...")
