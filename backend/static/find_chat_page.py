with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找聊天相关的id，比如 chat-messages, chat-input 之类的
import re
chat_ids = re.findall(r'id="(chat[^"]*)"', content)
print("=== chat相关的id ===")
for cid in chat_ids:
    print(f"  {cid}")

# 找"发送"按钮附近的内容
send_idx = content.find('onclick="sendMessage()"')
if send_idx != -1:
    # 往前找500个字符，看看有没有 section
    before = content[send_idx-500:send_idx]
    # 找最近的 section 开始
    section_start = before.rfind("<section")
    if section_start != -1:
        section_tag = before[section_start:section_start+100]
        print(f"\n=== 发送按钮附近的section ===")
        print(f"  {section_tag}")
