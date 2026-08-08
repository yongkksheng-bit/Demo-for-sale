with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re

# 找侧边栏导航的 onclick
nav_items = re.findall(r'onclick="showSection\(\'([^\']+)\'\)"', content)
print("=== 侧边栏导航的页面id ===")
for nav in nav_items:
    print(f"  {nav}")

# 找所有 section 的 id
section_ids = re.findall(r'<section[^>]*id="([^"]+)"', content)
print("\n=== 所有section的id ===")
for sid in section_ids:
    print(f"  {sid}")

# 检查匹配情况
print("\n=== 匹配检查 ===")
for nav in nav_items:
    if nav in section_ids:
        print(f"✅ {nav} 匹配")
    else:
        print(f"❌ {nav} 不匹配！")
