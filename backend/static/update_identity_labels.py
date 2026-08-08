with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. 修改身份选择模态框的标题
# 第一步：选择行业 → 你卖什么？
content = content.replace("选择行业", "你卖什么？")
content = content.replace("请选择你所在的行业", "请选择你所在的行业领域")

# 第二步：选择销售类型 → 你属于什么类型的销售？
content = content.replace("选择销售类型", "你属于什么类型的销售？")
content = content.replace("请选择你的销售类型", "请选择你的销售岗位类型")

# 2. 把各个功能里的行业label改成"客户行业"
# 销售话术
content = content.replace('<label class="block text-sm font-medium text-gray-700 mb-2">行业</label>\n                                    <select id="script-industry"', 
                          '<label class="block text-sm font-medium text-gray-700 mb-2">客户行业</label>\n                                    <select id="script-industry"')

# 异议处理
content = content.replace('<label class="block text-sm font-medium text-gray-700 mb-2">行业</label>\n                                    <select id="objection-industry"',
                          '<label class="block text-sm font-medium text-gray-700 mb-2">客户行业</label>\n                                    <select id="objection-industry"')

# 竞品对比
content = content.replace('<label class="block text-sm font-medium text-gray-700 mb-2">行业</label>\n                                        <select id="competitor-industry"',
                          '<label class="block text-sm font-medium text-gray-700 mb-2">客户行业</label>\n                                        <select id="competitor-industry"')

# 拜访清单
content = content.replace('<label class="block text-sm font-medium text-gray-700 mb-2">行业</label>\n                                        <select id="checklist-industry"',
                          '<label class="block text-sm font-medium text-gray-700 mb-2">客户行业</label>\n                                        <select id="checklist-industry"')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ 已修改：")
print("  1. 身份选择标题：第一步「你卖什么？」，第二步「你属于什么类型的销售？」")
print("  2. 工具箱4个功能的行业label都改成了「客户行业」")
