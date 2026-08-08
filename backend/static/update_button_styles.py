with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. 客户背调的生成按钮
# 找客户背调区域的生成按钮
research_start = content.find("id=\"research\"")
if research_start == -1:
    research_start = content.find("客户背调")
    
research_end = content.find("</section>", research_start)
research_content = content[research_start:research_end]

# 替换生成按钮样式
old_btn = 'bg-gray-900 text-white rounded-lg hover:bg-gray-800'
new_btn = 'bg-white border border-gray-200 text-gray-900 rounded-xl hover:bg-gray-50 hover:shadow-md transition-all font-medium shadow-sm'

# 客户背调生成按钮
research_content = research_content.replace(
    'onclick="generateResearch()" class="px-6 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition-colors"',
    'onclick="generateResearch()" class="px-6 py-2.5 bg-white border border-gray-200 text-gray-900 rounded-xl hover:bg-gray-50 hover:shadow-md transition-all text-sm font-medium shadow-sm"'
)

# 方案生成的生成按钮
solution_start = content.find("id=\"solution\"")
if solution_start == -1:
    solution_start = content.find("方案生成")

solution_end = content.find("</section>", solution_start)
solution_content = content[solution_start:solution_end]

# 方案生成按钮
solution_content = solution_content.replace(
    'onclick="generateSolution()" class="w-full py-3 bg-gray-900 text-white rounded-xl hover:bg-gray-800 transition-colors font-medium"',
    'onclick="generateSolution()" class="w-full py-3 bg-white border border-gray-200 text-gray-900 rounded-xl hover:bg-gray-50 hover:shadow-md transition-all font-medium shadow-sm"'
)

# 调整方案按钮
solution_content = solution_content.replace(
    'onclick="adjustSolution()" class="px-6 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition-colors"',
    'onclick="adjustSolution()" class="px-6 py-2.5 bg-white border border-gray-200 text-gray-900 rounded-xl hover:bg-gray-50 hover:shadow-md transition-all text-sm font-medium shadow-sm"'
)

# 智能对话的发送按钮
chat_start = content.find("id=\"chat\"")
if chat_start == -1:
    chat_start = content.find("智能对话")

chat_end = content.find("</section>", chat_start)
chat_content = content[chat_start:chat_end]

chat_content = chat_content.replace(
    'onclick="sendMessage()" class="px-6 py-3 bg-gray-900 text-white rounded-xl hover:bg-gray-800 transition-colors"',
    'onclick="sendMessage()" class="px-6 py-3 bg-white border border-gray-200 text-gray-900 rounded-xl hover:bg-gray-50 hover:shadow-md transition-all font-medium shadow-sm"'
)

# 替换回主内容
content = content[:research_start] + research_content + content[research_end:]
content = content[:solution_start] + solution_content + content[solution_end:]
content = content[:chat_start] + chat_content + content[chat_end:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ 已修改主要生成按钮为白色背景+阴影样式")
print("  - 客户背调生成按钮")
print("  - 方案生成按钮")
print("  - 调整方案按钮")
print("  - 智能对话发送按钮")
