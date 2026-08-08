with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re

# 找步骤指示器的圆圈样式
# 通常是 bg-gray-900 text-white 之类的
# 找所有 w-8 h-8 或者 w-10 h-10 的圆形步骤指示器

# 客户背调的步骤圆圈
# 找包含 "填写客户信息" 附近的圆圈
research_start = content.find("填写客户信息")
if research_start != -1:
    search_area = content[research_start - 500:research_start + 100]
    # 找圆形样式
    circles = re.findall(r'class="[^"]*rounded-full[^"]*"', search_area)
    print("客户背调附近的圆形样式：")
    for c in circles:
        print(f"  {c[:80]}...")

# 方案生成的步骤指示器
solution_start = content.find("步骤")
if solution_start != -1:
    search_area = content[solution_start:solution_start + 1000]
    circles = re.findall(r'class="[^"]*rounded-full[^"]*"', search_area)
    print("\n方案生成附近的圆形样式：")
    for c in circles:
        print(f"  {c[:80]}...")
