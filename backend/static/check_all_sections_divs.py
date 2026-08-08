with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re

# 找所有 section 的位置
sections = []
pos = 0
while True:
    idx = content.find("<section", pos)
    if idx == -1:
        break
    # 找 id
    id_match = re.search(r'id="([^"]*)"', content[idx:idx+200])
    sid = id_match.group(1) if id_match else "unknown"
    sections.append((idx, sid))
    pos = idx + 1

# 逐个检查每个 section 的 div 数量
print("=== 每个 section 的 div 数量 ===")
total_divs = 0
total_div_ends = 0
for i, (start, sid) in enumerate(sections):
    if i < len(sections) - 1:
        end = sections[i+1][0]
    else:
        end = len(content)
    
    section_content = content[start:end]
    divs = len(re.findall(r'<div', section_content))
    div_ends = len(re.findall(r'</div>', section_content))
    diff = div_ends - divs
    total_divs += divs
    total_div_ends += div_ends
    
    status = "✅" if diff == 0 else "❌"
    print(f"{status} {sid}: 开始 {divs}, 结束 {div_ends}, 差值 {diff}")

print(f"\n总计: 开始 {total_divs}, 结束 {total_div_ends}, 差值 {total_div_ends - total_divs}")
