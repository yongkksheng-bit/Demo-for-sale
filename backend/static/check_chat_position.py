with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找 id="chat" 的行
for i, line in enumerate(lines):
    if 'id="chat"' in line:
        print(f"第 {i+1} 行: {line.strip()[:100]}")
        
        # 往前找10行，看看在什么里面
        print("\n往前10行:")
        for j in range(max(0, i-10), i):
            print(f"  {j+1}: {lines[j].rstrip()[:80]}")
        
        # 往后找10行
        print("\n往后10行:")
        for j in range(i+1, min(len(lines), i+11)):
            print(f"  {j+1}: {lines[j].rstrip()[:80]}")
        break
