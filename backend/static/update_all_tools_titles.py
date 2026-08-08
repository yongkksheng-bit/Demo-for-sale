with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 改其他几个工具的右侧标题
# 异议处理
content = content.replace(
    '<h3 class="text-lg font-semibold text-gray-900 mb-1">异议处理助手</h3>',
    '<h3 class="text-xl font-bold text-gray-900 mb-2">异议处理助手</h3>'
)
content = content.replace(
    '<p class="text-gray-400 text-sm mb-6">专业应对客户疑问，化解顾虑</p>',
    '<p class="text-gray-500 text-base mb-6">专业应对客户疑问，化解顾虑</p>'
)

# 竞品对比
content = content.replace(
    '<h3 class="text-lg font-semibold text-gray-900 mb-1">竞品对比分析</h3>',
    '<h3 class="text-xl font-bold text-gray-900 mb-2">竞品对比分析</h3>'
)
content = content.replace(
    '<p class="text-gray-400 text-sm mb-6">分析我们与竞品的差异化优势</p>',
    '<p class="text-gray-500 text-base mb-6">分析我们与竞品的差异化优势</p>'
)

# 拜访清单
content = content.replace(
    '<h3 class="text-lg font-semibold text-gray-900 mb-1">拜访准备清单</h3>',
    '<h3 class="text-xl font-bold text-gray-900 mb-2">拜访准备清单</h3>'
)
content = content.replace(
    '<p class="text-gray-400 text-sm mb-6">拜访前的准备工作检查清单</p>',
    '<p class="text-gray-500 text-base mb-6">拜访前的准备工作检查清单</p>'
)

# ROI计算器
content = content.replace(
    '<h3 class="text-lg font-semibold text-gray-900 mb-1">ROI 投资回报计算器</h3>',
    '<h3 class="text-xl font-bold text-gray-900 mb-2">ROI 投资回报计算器</h3>'
)
content = content.replace(
    '<p class="text-gray-400 text-sm mb-6">快速计算方案的投资回报率</p>',
    '<p class="text-gray-500 text-base mb-6">快速计算方案的投资回报率</p>'
)

# 右侧内容区域内边距加大
# 找右侧内容的容器
idx = content.find('<!-- 右侧内容区 -->')
if idx != -1:
    print(f"右侧内容区位置: {idx}")
    # 看看后面的 div
    print(f"内容: {content[idx:idx+200]}")
    
    # 替换右侧内容容器的内边距
    # 先找到右侧容器的 class
    import re
    match = re.search(r'<div class="([^"]*)">', content[idx:idx+200])
    if match:
        old_class = match.group(1)
        print(f"旧的 class: {old_class}")
        
        # 加上 p-6 或者加大内边距
        # 先看看现在的内边距
        if 'p-' in old_class or 'py-' in old_class or 'px-' in old_class:
            print("已有内边距类")
        else:
            print("没有内边距类，需要加上")

# 保存
with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("\n✅ 已更新所有工具的右侧标题样式")
