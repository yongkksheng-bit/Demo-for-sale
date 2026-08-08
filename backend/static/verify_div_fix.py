with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re

divs = len(re.findall(r'<div', content))
div_ends = len(re.findall(r'</div>', content))
print(f"全站 div 标签:")
print(f"  开始标签: {divs} 个")
print(f"  结束标签: {div_ends} 个")
print(f"  差值: {div_ends - divs} 个")

if divs == div_ends:
    print("✅ div 标签完全对等！")
else:
    print("❌ 还有不对等的地方")

# 再检查每个 section
sections = []
pos = 0
while True:
    idx = content.find("<section", pos)
    if idx == -1:
        break
    id_match = re.search(r'id="([^"]*)"', content[idx:idx+200])
    sid = id_match.group(1) if id_match else "unknown"
    sections.append((idx, sid))
    pos = idx + 1

print("\n=== 每个 section 的 div 数量 ===")
for i, (start, sid) in enumerate(sections):
    if i < len(sections) - 1:
        end = sections[i+1][0]
    else:
        end = len(content)
    
    section_content = content[start:end]
    d = len(re.findall(r'<div', section_content))
    de = len(re.findall(r'</div>', section_content))
    diff = de - d
    status = "✅" if diff == 0 else "❌"
    print(f"{status} {sid}: 开始 {d}, 结束 {de}, 差值 {diff}")
