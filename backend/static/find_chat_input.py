with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找 chat-input
for i, line in enumerate(lines):
    if 'id="chat-input"' in line:
        print(f"chat-input 在第 {i+1} 行")
        # 显示前后10行
        print("\n前后10行：")
        for j in range(max(0, i-5), min(len(lines), i+15)):
            print(f"  第 {j+1} 行: {lines[j].rstrip()[:80]}")
        break
