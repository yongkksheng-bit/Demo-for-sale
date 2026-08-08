with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 1. 提取智能对话的内容（第1159行到第1210行，索引1158到1209）
chat_content = lines[1158:1210]

# 加上 chat div 的结束标签（因为原来的丢了）
chat_content.append("            </div>\n")

print(f"智能对话内容共 {len(chat_content)} 行")

# 2. 删除原来位置的智能对话内容（第1159行到第1210行）
del lines[1158:1210]

print(f"删除后剩余 {len(lines)} 行")

# 3. 找到销售工具箱 section 的结束位置
tools_end = -1
for i, line in enumerate(lines):
    if i > 1158 and '</section>' in line:
        tools_end = i
        break

if tools_end != -1:
    print(f"销售工具箱结束于第 {tools_end+1} 行")
    
    # 4. 把智能对话插入到销售工具箱后面
    # 先加个空行和注释
    chat_with_comment = [
        "\n",
        "        <!-- 智能对话 -->\n",
    ] + chat_content
    
    # 插入到 tools_end + 1 的位置
    for j, line in enumerate(chat_with_comment):
        lines.insert(tools_end + 1 + j, line)
    
    print(f"已将智能对话插入到第 {tools_end+2} 行")

# 5. 检查 div 数量
import re
divs = 0
div_ends = 0
for line in lines:
    divs += line.count("<div")
    div_ends += line.count("</div>")

print(f"\n全站 div 标签: 开始 {divs}, 结束 {div_ends}, 差值 {div_ends - divs}")

if divs == div_ends:
    print("✅ div 标签对等！")
else:
    print("❌ div 标签不对等")

# 保存
with open("index.html", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("\n✅ 已修复智能对话位置")
