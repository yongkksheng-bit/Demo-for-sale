with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 直接替换三个步骤的文字，加上 whitespace-nowrap 和 flex-shrink-0
# 步骤1
content = content.replace(
    '<span class="ml-2 font-medium text-dark">你卖什么？</span>',
    '<span class="ml-2 font-medium text-gray-900 text-sm whitespace-nowrap">你卖什么</span>'
)

# 步骤2
content = content.replace(
    '<span class="ml-2 text-gray-500 text-sm">选择场景</span>',
    '<span class="ml-2 text-gray-500 text-sm whitespace-nowrap">选择场景</span>'
)

# 步骤3
content = content.replace(
    '<span class="ml-2 text-gray-500 text-sm">生成方案</span>',
    '<span class="ml-2 text-gray-500 text-sm whitespace-nowrap">生成方案</span>'
)

# 给每个步骤的容器加上 flex-shrink-0
content = content.replace(
    '<div class="flex items-center">\n                                    <div id="step1-dot"',
    '<div class="flex items-center flex-shrink-0">\n                                    <div id="step1-dot"'
)
content = content.replace(
    '<div class="flex items-center">\n                                    <div id="step2-dot"',
    '<div class="flex items-center flex-shrink-0">\n                                    <div id="step2-dot"'
)
content = content.replace(
    '<div class="flex items-center">\n                                    <div id="step3-dot"',
    '<div class="flex items-center flex-shrink-0">\n                                    <div id="step3-dot"'
)

# 圆点加上 flex-shrink-0
content = content.replace(
    'id="step1-dot" class="w-8 h-8 rounded-full',
    'id="step1-dot" class="w-7 h-7 rounded-full flex-shrink-0'
)
content = content.replace(
    'id="step2-dot" class="w-8 h-8 rounded-full',
    'id="step2-dot" class="w-7 h-7 rounded-full flex-shrink-0'
)
content = content.replace(
    'id="step3-dot" class="w-8 h-8 rounded-full',
    'id="step3-dot" class="w-7 h-7 rounded-full flex-shrink-0'
)

# 保存
with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ 已更新步骤指示器")
print("  - 文字不换行（whitespace-nowrap）")
print("  - 圆点缩小（w-8 → w-7）")
print("  - 去掉问号，节省空间")
print("  - 加上 flex-shrink-0 防止压缩")
