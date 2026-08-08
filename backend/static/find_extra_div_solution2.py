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
            for j in range(i, max(0, i-5), -1):
                if '<section' in lines[j]:
                    solution_start = j
                    break
            break

print(f"方案生成开始于第 {solution_start+1} 行")

# 逐行检查 div 数量，找到哪里多了一个
div_count = 0
extra_div_line = -1
for i in range(solution_start, len(lines)):
    line = lines[i]
    div_count += line.count("<div")
    div_count -= line.count("</div>")
    
    # 遇到 </section> 就停止
    if '</section>' in line and i > solution_start + 5:
        print(f"方案生成结束于第 {i+1} 行，最终 div 计数: {div_count}")
        break
    
    # 如果 div_count 变成负数，说明这里多了一个 </div>
    if div_count < 0:
        extra_div_line = i
        print(f"❌ 第 {i+1} 行: div 计数变成 {div_count}，多了一个 </div>")
        print(f"   内容: {line.strip()[:80]}")
        
        # 显示上下文
        print("\n   上下文:")
        for j in range(max(0, i-3), min(len(lines), i+4)):
            marker = "👉" if j == i else "  "
            print(f"   {marker} {j+1}: {lines[j].rstrip()[:80]}")
        break

if extra_div_line != -1:
    # 删掉这个多余的 </div>
    del lines[extra_div_line]
    print(f"\n✅ 已删除第 {extra_div_line+1} 行多余的 </div>")
    
    # 重新检查
    divs = 0
    div_ends = 0
    for line in lines:
        divs += line.count("<div")
        div_ends += line.count("</div>")
    
    print(f"全站 div 标签: 开始 {divs}, 结束 {div_ends}, 差值 {div_ends - divs}")
    
    if divs == div_ends:
        print("✅ div 标签对等！")
    
    # 保存
    with open("index.html", "w", encoding="utf-8") as f:
        f.writelines(lines)
