with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 提取智能对话的内容（第1159行到第1212行，索引1158到1211）
chat_lines = lines[1158:1212]
print(f"提取了 {len(chat_lines)} 行智能对话内容")
print("\n前5行：")
for i in range(5):
    print(f"  {chat_lines[i].rstrip()[:80]}")
print("\n后5行：")
for i in range(max(0, len(chat_lines)-5), len(chat_lines)):
    print(f"  {chat_lines[i].rstrip()[:80]}")

# 保存到临时文件
with open("chat_temp.html", "w", encoding="utf-8") as f:
    f.writelines(chat_lines)

print("\n✅ 已保存到 chat_temp.html")
