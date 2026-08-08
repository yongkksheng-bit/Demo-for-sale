with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 修复剩下的下拉框选项
content = content.replace("请你卖什么？", "请选择行业")

# 把"所属行业"改成"客户行业"
content = content.replace(">所属行业<", ">客户行业<")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ 已修复：")
print("  1. 剩下的下拉框选项「请你卖什么？」→「请选择行业」")
print("  2. 「所属行业」→「客户行业」")
