with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

divs = 0
div_ends = 0
for line in lines:
    divs += line.count("<div")
    div_ends += line.count("</div>")

print(f"全站 div 标签:")
print(f"  开始标签: {divs} 个")
print(f"  结束标签: {div_ends} 个")
print(f"  差值: {div_ends - divs} 个")

if divs == div_ends:
    print("✅ div 标签完全对等！")
else:
    print("❌ 还有不对等的地方")
    
    # 逐行检查，找到哪里开始不对
    count = 0
    for i, line in enumerate(lines):
        count += line.count("<div")
        count -= line.count("</div>")
        if count < 0:
            print(f"\n❌ 第 {i+1} 行: div 计数变成 {count}，多了一个 </div>")
            print(f"   内容: {line.strip()[:80]}")
            
            # 显示上下文
            print("\n   上下文:")
            for j in range(max(0, i-3), min(len(lines), i+4)):
                marker = "👉" if j == i else "  "
                print(f"   {marker} {j+1}: {lines[j].rstrip()[:80]}")
            break
