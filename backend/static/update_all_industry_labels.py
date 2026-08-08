with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 客户背调的行业
import re
# 找客户背调区域的行业label
research_start = content.find("客户背调")
if research_start != -1:
    # 找附近的行业label
    search_area = content[research_start:research_start + 2000]
    # 替换
    new_area = search_area.replace('>行业<', '>客户行业<')
    content = content[:research_start] + new_area + content[research_start + 2000:]
    print("✅ 客户背调行业label已改")

# 方案生成的行业
solution_start = content.find("方案生成")
if solution_start != -1:
    search_area = content[solution_start:solution_start + 3000]
    new_area = search_area.replace('>行业<', '>客户行业<')
    content = content[:solution_start] + new_area + content[solution_start + 3000:]
    print("✅ 方案生成行业label已改")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("\n✅ 所有行业label都改成了「客户行业」")
