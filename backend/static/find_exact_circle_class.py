with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re

# 找所有 bg-gray-900 text-white 的圆形
pattern = r'class="([^"]*bg-gray-900[^"]*text-white[^"]*rounded-full[^"]*)"'
matches = re.findall(pattern, content)
print(f"找到 {len(matches)} 个黑底白字的圆形：")
for i, m in enumerate(matches[:5]):
    print(f"\n{i+1}. {m}")
