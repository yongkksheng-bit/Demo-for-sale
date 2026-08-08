with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re

# 找所有 section 的 id 和标题
sections = []
for match in re.finditer(r'<section[^>]*id="([^"]*)"[^>]*class="section hidden[^"]*"[^>]*>', content):
    sid = match.group(1)
    start = match.end()
    
    # 找后面的 h2 标题
    h2_match = re.search(r'<h2[^>]*>([^<]*)</h2>', content[start:start+500])
    if h2_match:
        title = h2_match.group(1).strip()
    else:
        title = "(无标题)"
    
    # 找 class
    class_match = re.search(r'class="([^"]*)"', match.group())
    cls = class_match.group(1) if class_match else ""
    
    sections.append((sid, title, cls))

print("=== 所有模块的头部样式 ===")
for sid, title, cls in sections:
    print(f"  {sid}:")
    print(f"    标题: {title}")
    print(f"    class: {cls[:60]}...")
    print()
