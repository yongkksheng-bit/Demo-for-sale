with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找智能对话的输入框，那应该是智能对话的最后一部分
chat_input_end = -1
for i, line in enumerate(lines):
    if 'chat-input' in line or '发送' in line and i > 1165:
        # 看看是不是智能对话的输入框
        chat_input_end = i

# 找回到顶部按钮，那应该是在所有 section 之后
back_to_top = -1
for i, line in enumerate(lines):
    if 'back-to-top' in line or '回到顶部' in line:
        back_to_top = i
        break

if back_to_top != -1:
    print(f"回到顶部按钮在第 {back_to_top+1} 行")
    # 智能对话应该在回到顶部按钮之前结束
    # 在回到顶部按钮之前加上 </section>
    
    # 先看看回到顶部按钮前面的内容
    print("\n回到顶部按钮前面5行：")
    for i in range(max(0, back_to_top-5), back_to_top+1):
        print(f"  {i+1}: {lines[i].rstrip()[:80]}")
    
    # 在回到顶部按钮之前插入 </section>
    # 先找到合适的位置，就是回到顶部按钮的上一个空行
    insert_pos = back_to_top
    for i in range(back_to_top - 1, 1165, -1):
        if lines[i].strip() == "":
            insert_pos = i
            break
    
    print(f"\n在第 {insert_pos+1} 行插入 </section>")
    
    # 插入
    lines.insert(insert_pos, "        </section>\n")
    
    # 保存
    with open("index.html", "w", encoding="utf-8") as f:
        f.writelines(lines)
    
    print("\n✅ 已给智能对话加上结束标签")
else:
    print("❌ 没找到回到顶部按钮")
