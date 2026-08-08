with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找各个关键位置
positions = {}
for i, line in enumerate(lines):
    if 'id="solution"' in line:
        positions['solution_start'] = i+1
    if 'id="tools"' in line and '<section' in lines[max(0,i-2):i+2].join(''):
        positions['tools_start'] = i+1
    if 'id="chat"' in line:
        positions['chat_start'] = i+1
    if '</section>' in line:
        # 记录每个 </section> 的位置
        if 'section_ends' not in positions:
            positions['section_ends'] = []
        positions['section_ends'].append(i+1)

print("=== 关键位置 ===")
for k, v in positions.items():
    if k != 'section_ends':
        print(f"  {k}: 第 {v} 行")

print(f"\n  </section> 位置: {positions.get('section_ends', [])}")

# 判断 chat 在 solution section 里面还是外面
solution_start = positions.get('solution_start', 0)
solution_end = None
for se in positions.get('section_ends', []):
    if se > solution_start:
        solution_end = se
        break

print(f"\nsolution section: 第 {solution_start} 行开始，第 {solution_end} 行结束")
print(f"chat div: 第 {positions.get('chat_start', 0)} 行开始")

if positions.get('chat_start', 0) < solution_end:
    print("❌ chat div 在 solution section 里面！这就是bug！")
else:
    print("✅ chat div 在 solution section 外面")
