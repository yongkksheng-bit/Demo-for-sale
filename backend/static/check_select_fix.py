with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 检查还有没有"你卖什么"出现在下拉框里
import re

# 找所有 select 里的 option
options = re.findall(r'<option[^>]*>(.*?)</option>', content)
weird_options = [o for o in options if "卖什么" in o or "销售类型" in o]

if weird_options:
    print("❌ 还有错误的下拉框选项：")
    for o in weird_options:
        print(f"  {o}")
else:
    print("✅ 下拉框选项都正常")

# 检查客户背调的行业label
if "客户行业" in content:
    print("✅ 客户背调行业label已改成「客户行业」")
else:
    print("❌ 客户背调行业label没改")
    
# 检查所属行业这个label还在不在
if "所属行业" in content:
    print("⚠️  还有「所属行业」的label，需要改成「客户行业」")
