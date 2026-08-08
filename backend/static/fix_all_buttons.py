with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re

# 找所有用 bg-gradient-primary 的按钮
gradient_btns = re.findall(r'<button[^>]*bg-gradient-primary[^>]*>', content)
print(f"用 bg-gradient-primary 的按钮数量: {len(gradient_btns)}")

# 逐个替换
# 方案生成按钮
solution_start = content.find("id=\"solution\"")
solution_end = content.find("</section>", solution_start)
solution_content = content[solution_start:solution_end]

# 找生成按钮
btn_match = re.search(r'<button[^>]*generateSolution[^>]*>.*?</button>', solution_content, re.DOTALL)
if btn_match:
    old_btn = btn_match.group()
    # 提取里面的内容
    inner_match = re.search(r'<button[^>]*>(.*?)</button>', old_btn, re.DOTALL)
    if inner_match:
        inner = inner_match.group(1)
        new_btn = f'<button onclick="generateSolution()" id="generate-btn" class="w-full py-4 bg-white border border-gray-200 text-gray-900 rounded-xl hover:bg-gray-50 hover:shadow-md transition-all font-semibold shadow-sm flex items-center justify-center space-x-2">{inner}</button>'
        solution_content = solution_content.replace(old_btn, new_btn)
        print("✅ 方案生成按钮已改成白色样式")

# 调整方案按钮
adjust_match = re.search(r'<button[^>]*adjustSolution[^>]*>.*?</button>', solution_content, re.DOTALL)
if adjust_match:
    old_btn = adjust_match.group()
    inner_match = re.search(r'<button[^>]*>(.*?)</button>', old_btn, re.DOTALL)
    if inner_match:
        inner = inner_match.group(1)
        new_btn = f'<button onclick="adjustSolution()" class="px-6 py-2.5 bg-white border border-gray-200 text-gray-900 rounded-xl hover:bg-gray-50 hover:shadow-md transition-all text-sm font-medium shadow-sm">{inner}</button>'
        solution_content = solution_content.replace(old_btn, new_btn)
        print("✅ 调整方案按钮已改成白色样式")

# 智能对话发送按钮
chat_start = content.find("id=\"chat\"")
chat_end = content.find("</section>", chat_start)
chat_content = content[chat_start:chat_end]

send_match = re.search(r'<button[^>]*sendMessage[^>]*>.*?</button>', chat_content, re.DOTALL)
if send_match:
    old_btn = send_match.group()
    inner_match = re.search(r'<button[^>]*>(.*?)</button>', old_btn, re.DOTALL)
    if inner_match:
        inner = inner_match.group(1)
        new_btn = f'<button onclick="sendMessage()" class="px-6 py-3 bg-white border border-gray-200 text-gray-900 rounded-xl hover:bg-gray-50 hover:shadow-md transition-all font-medium shadow-sm">{inner}</button>'
        chat_content = chat_content.replace(old_btn, new_btn)
        print("✅ 智能对话发送按钮已改成白色样式")

# 替换回去
content = content[:solution_start] + solution_content + content[solution_end:]
content = content[:chat_start] + chat_content + content[chat_end:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("\n✅ 所有主要按钮已改成白色样式")
