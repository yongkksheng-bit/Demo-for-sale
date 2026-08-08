with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找 id="chat" 的位置
for i, line in enumerate(lines):
    if 'id="chat"' in line:
        print(f"id='chat' 在第 {i+1} 行")
        # 往前找10行，看看在哪个 section 里
        print("\n往前10行：")
        for j in range(max(0, i-10), i+1):
            print(f"  {j+1}: {lines[j].rstrip()[:80]}")
        
        # 往后找5行
        print("\n往后5行：")
        for j in range(i+1, min(len(lines), i+6)):
            print(f"  {j+1}: {lines[j].rstrip()[:80]}")
        break
