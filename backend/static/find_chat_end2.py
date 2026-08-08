with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找智能对话的开始
chat_start = -1
for i, line in enumerate(lines):
    if 'id="chat"' in line:
        chat_start = i
        break

print(f"智能对话开始于第 {chat_start+1} 行")

# 找智能对话的结束（找 </section>）
section_count = 1
chat_end = -1
for i in range(chat_start + 1, len(lines)):
    line = lines[i]
    section_count += line.count("<section")
    section_count -= line.count("</section>")
    if section_count == 0:
        chat_end = i
        break

if chat_end != -1:
    print(f"智能对话结束于第 {chat_end+1} 行")
    print(f"结束行内容: {lines[chat_end].rstrip()[:80]}")
else:
    print(f"❌ 没找到智能对话的结束标签，section_count = {section_count}")
    # 看看后面几行
    print("\n后面20行：")
    for i in range(chat_start + 1, min(len(lines), chat_start + 30)):
        print(f"  {i+1}: {lines[i].rstrip()[:80]}")
