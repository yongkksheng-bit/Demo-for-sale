with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. 左侧工具列表：字体加大
# 工具标题：text-sm → text-base
# 工具副标题：text-xs → text-sm
content = content.replace(
    '<div class="font-medium text-gray-900 text-sm">销售话术</div>',
    '<div class="font-medium text-gray-900 text-base">销售话术</div>'
)
content = content.replace(
    '<div class="text-xs text-gray-400">生成专业话术</div>',
    '<div class="text-sm text-gray-500">生成专业话术</div>'
)

content = content.replace(
    '<div class="font-medium text-gray-900 text-sm">异议处理</div>',
    '<div class="font-medium text-gray-900 text-base">异议处理</div>'
)
content = content.replace(
    '<div class="text-xs text-gray-400">应对客户疑问</div>',
    '<div class="text-sm text-gray-500">应对客户疑问</div>'
)

content = content.replace(
    '<div class="font-medium text-gray-900 text-sm">竞品对比</div>',
    '<div class="font-medium text-gray-900 text-base">竞品对比</div>'
)
content = content.replace(
    '<div class="text-xs text-gray-400">分析差异化优势</div>',
    '<div class="text-sm text-gray-500">分析差异化优势</div>'
)

content = content.replace(
    '<div class="font-medium text-gray-900 text-sm">拜访清单</div>',
    '<div class="font-medium text-gray-900 text-base">拜访清单</div>'
)
content = content.replace(
    '<div class="text-xs text-gray-400">拜访准备检查</div>',
    '<div class="text-sm text-gray-500">拜访准备检查</div>'
)

content = content.replace(
    '<div class="font-medium text-gray-900 text-sm">ROI计算器</div>',
    '<div class="font-medium text-gray-900 text-base">ROI 计算器</div>'
)
content = content.replace(
    '<div class="text-xs text-gray-400">投资回报分析</div>',
    '<div class="text-sm text-gray-500">投资回报分析</div>'
)

# 2. 右侧内容区域：标题加大
# 子标题：text-lg → text-xl
# 副标题：text-gray-400 text-sm → text-gray-500 text-base
content = content.replace(
    '<h3 class="text-lg font-semibold text-gray-900 mb-1">销售话术生成</h3>',
    '<h3 class="text-xl font-bold text-gray-900 mb-2">销售话术生成</h3>'
)
content = content.replace(
    '<p class="text-gray-400 text-sm mb-6">根据行业和场景生成专业销售话术</p>',
    '<p class="text-gray-500 text-base mb-6">根据行业和场景生成专业销售话术</p>'
)

# 左侧工具列表宽度加大一点
content = content.replace(
    '<div class="w-56 border-r border-gray-100 py-4">',
    '<div class="w-60 border-r border-gray-100 py-6">'
)

# 右侧内容区域内边距加大
# 先看看右侧内容区域的 div
# 找一下右侧内容的容器
idx = content.find('tool-content-script')
if idx != -1:
    # 往前找右侧容器
    right_start = content.rfind('<div', 0, idx)
    print(f"右侧容器开始位置: {right_start}")
    print(f"内容: {content[right_start:right_start+100]}")

# 保存
with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("\n✅ 已调整销售工具箱字体大小")
print("  - 左侧工具标题：text-sm → text-base")
print("  - 左侧工具副标题：text-xs → text-sm")
print("  - 右侧内容标题：text-lg → text-xl")
print("  - 右侧内容副标题：text-sm → text-base")
print("  - 左侧列表宽度：w-56 → w-60")
print("  - 左侧列表内边距：py-4 → py-6")
