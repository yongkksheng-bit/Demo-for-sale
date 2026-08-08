with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找到我刚才加的那个多余的 </div>
# 在智能对话的最后
chat_start = -1
for i, line in enumerate(lines):
    if 'id="chat"' in line:
        chat_start = i
        break

if chat_start != -1:
    print(f"智能对话开始于第 {chat_start+1} 行")
    
    # 找 chat div 的结束
    div_count = 1
    chat_end = -1
    for i in range(chat_start + 1, len(lines)):
        line = lines[i]
        div_count += line.count("<div")
        div_count -= line.count("</div>")
        if div_count == 0:
            chat_end = i
            break
    
    if chat_end != -1:
        print(f"智能对话结束于第 {chat_end+1} 行")
        print(f"结束行内容: {lines[chat_end].rstrip()[:80]}")
    else:
        print("❌ 没找到结束位置，div_count = {div_count}")

# 检查全站 div 数量
import re
divs = 0
div_ends = 0
for line in lines:
    divs += line.count("<div")
    div_ends += line.count("</div>")

print(f"\n全站 div 标签: 开始 {divs}, 结束 {div_ends}, 差值 {div_ends - divs}")
