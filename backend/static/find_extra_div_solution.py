with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找方案生成 section 的开始
solution_start = -1
for i, line in enumerate(lines):
    if '<section' in line and 'id="solution"' in line:
        solution_start = i
        break

if solution_start == -1:
    # 换个方式找
    for i, line in enumerate(lines):
        if 'id="solution"' in line:
            # 往前找 section
            for j in range(i, max(0, i-5), -1):
                if '<section' in lines[j]:
                    solution_start = j
                    break
            break

print(f"方案生成 section 开始于第 {solution_start+1} 行")

# 逐行检查 div 数量，找到哪里开始不对
div_count = 0
for i in range(solution_start, len(lines)):
    line = lines[i]
    div_count += line.count("<div")
    div_count -= line.count("</div>")
    
    # 如果 div_count 变成负数，说明这里多了一个 </div>
    if div_count < 0:
        print(f"❌ 第 {i+1} 行: div 计数变成 {div_count}，多了一个 </div>")
        print(f"   内容: {line.strip()[:80]}")
        
        # 显示前后5行
        print("\n   上下文:")
        for j in range(max(0, i-3), min(len(lines), i+4)):
            marker = "👉" if j == i else "  "
            print(f"   {marker} {j+1}: {lines[j].rstrip()[:80]}")
        break
    
    # 遇到 </section> 就停止
    if '</section>' in line and i > solution_start + 5:
        print(f"方案生成 section 结束于第 {i+1} 行，最终 div 计数: {div_count}")
        break
