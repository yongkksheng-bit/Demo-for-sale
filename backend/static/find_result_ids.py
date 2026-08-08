with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找方案生成的结果区域
# 找 id="solution-result" 或者类似的
import re
result_ids = re.findall(r'id="(solution[^"]*)"', content)
print("方案生成相关的id：")
for rid in result_ids:
    print(f"  {rid}")

# 找客户背调的结果区域
research_ids = re.findall(r'id="(research[^"]*)"', content)
print("\n客户背调相关的id：")
for rid in research_ids:
    print(f"  {rid}")
