with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找方案生成结果区域
solution_start = content.find("id=\"solution\"")
if solution_start == -1:
    solution_start = content.find("方案生成")
solution_end = content.find("</section>", solution_start)
solution_content = content[solution_start:solution_end]

# 找 bg-gray-50 的地方
import re
gray50s = re.findall(r'class="[^"]*bg-gray-50[^"]*"', solution_content)
print("方案生成里的 bg-gray-50 元素：")
for g in gray50s[:5]:
    print(f"  {g[:80]}...")
