with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 智能对话开始于第1158-1159行（id="chat"）
chat_start_line = 1158  # 索引从0开始

# 找到 chat div 的结束位置
# 从 chat_start_line 开始，跟踪 div 的嵌套层级
div_count = 0
chat_end_line = -1

for i in range(chat_start_line, len(lines)):
    line = lines[i]
    # 统计这一行的 <div 和 </div>
    opens = line.count("<div")
    closes = line.count("</div>")
    
    # 第一行是开始，先加1
    if i == chat_start_line:
        div_count = 1  # 已经有一个开始了
        continue
    
    div_count += opens
    div_count -= closes
    
    if div_count == 0:
        chat_end_line = i
        break

if chat_end_line != -1:
    print(f"智能对话 div 开始于第 {chat_start_line+1} 行")
    print(f"智能对话 div 结束于第 {chat_end_line+1} 行")
    print(f"共 {chat_end_line - chat_start_line + 1} 行")
    
    # 看看结束行附近的内容
    print("\n结束行附近：")
    for i in range(max(0, chat_end_line-2), min(len(lines), chat_end_line+3)):
        print(f"  第 {i+1} 行: {lines[i].rstrip()[:80]}")
else:
    print("❌ 没找到智能对话的结束位置")
