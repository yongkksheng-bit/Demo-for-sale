with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 客户背调的卡片/容器
# 找客户背调区域的主要容器
research_start = content.find("id=\"research\"")
if research_start == -1:
    research_start = content.find("客户背调")
research_end = content.find("</section>", research_start)
research_content = content[research_start:research_end]

# 把 bg-gray-50 的结果区域改成带边框阴影的白色卡片
research_content = research_content.replace(
    'bg-gray-50 rounded-xl p-6',
    'bg-white border border-gray-200 rounded-xl p-6 shadow-sm'
)

# 方案生成的结果区域
solution_start = content.find("id=\"solution\"")
if solution_start == -1:
    solution_start = content.find("方案生成")
solution_end = content.find("</section>", solution_start)
solution_content = content[solution_start:solution_end]

solution_content = solution_content.replace(
    'bg-gray-50 rounded-xl p-6',
    'bg-white border border-gray-200 rounded-xl p-6 shadow-sm'
)

# 智能对话的消息气泡
# 这个暂时不改，保持聊天风格

# 替换回去
content = content[:research_start] + research_content + content[research_end:]
content = content[:solution_start] + solution_content + content[solution_end:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ 已修改结果区域卡片样式")
print("  - 客户背调结果区域")
print("  - 方案生成结果区域")
print("  改成：白色背景 + 浅灰边框 + 轻微阴影")
