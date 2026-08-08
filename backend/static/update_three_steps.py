with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找到三步上手的三个卡片（第286-306行左右）
# 旧的样式：黑底方形数字，死板
# 新的样式：圆形数字，悬浮效果，更活跃

# 第286-292行：第一个卡片
# 第293-299行：第二个卡片
# 第300-306行：第三个卡片

# 替换三个卡片的内容
old_card1 = '''                        <div class="bg-white border border-gray-200 rounded-xl p-6 hover:shadow-md transition-shadow">
                            <div class="w-12 h-12 bg-gray-900 rounded-lg flex items-center justify-center mb-4">
                                <span class="text-white text-xl font-bold">1</span>
                            </div>
                            <h4 class="font-bold text-gray-900 mb-2">输入客户信息</h4>
                            <p class="text-gray-500 text-sm">填写公司名称、行业、拜访对象。不知道也没关系，公司名就够了。</p>
                        </div>'''

new_card1 = '''                        <div class="bg-white border border-gray-200 rounded-2xl p-6 hover:shadow-lg hover:-translate-y-1 transition-all duration-300">
                            <div class="w-14 h-14 bg-gradient-to-br from-gray-800 to-gray-900 rounded-full flex items-center justify-center mb-5 shadow-lg">
                                <span class="text-white text-2xl font-bold">1</span>
                            </div>
                            <h4 class="text-lg font-bold text-gray-900 mb-2">输入客户信息</h4>
                            <p class="text-gray-500 text-sm leading-relaxed">填写公司名称、行业、拜访对象。不知道也没关系，公司名就够了。</p>
                        </div>'''

old_card2 = '''                        <div class="bg-white border border-gray-200 rounded-xl p-6 hover:shadow-md transition-shadow">
                            <div class="w-12 h-12 bg-gray-900 rounded-lg flex items-center justify-center mb-4">
                                <span class="text-white text-xl font-bold">2</span>
                            </div>
                            <h4 class="font-bold text-gray-900 mb-2">AI 一键生成</h4>
                            <p class="text-gray-500 text-sm">点击生成按钮，AI 自动分析，30 秒出结果，不用等。</p>
                        </div>'''

new_card2 = '''                        <div class="bg-white border border-gray-200 rounded-2xl p-6 hover:shadow-lg hover:-translate-y-1 transition-all duration-300">
                            <div class="w-14 h-14 bg-gradient-to-br from-gray-800 to-gray-900 rounded-full flex items-center justify-center mb-5 shadow-lg">
                                <span class="text-white text-2xl font-bold">2</span>
                            </div>
                            <h4 class="text-lg font-bold text-gray-900 mb-2">AI 一键生成</h4>
                            <p class="text-gray-500 text-sm leading-relaxed">点击生成按钮，AI 自动分析，30 秒出结果，不用等。</p>
                        </div>'''

old_card3 = '''                        <div class="bg-white border border-gray-200 rounded-xl p-6 hover:shadow-md transition-shadow">
                            <div class="w-12 h-12 bg-gray-900 rounded-lg flex items-center justify-center mb-4">
                                <span class="text-white text-xl font-bold">3</span>
                            </div>
                            <h4 class="font-bold text-gray-900 mb-2">直接拿去用</h4>
                            <p class="text-gray-500 text-sm">一键复制，拜访前 5 分钟就能准备好，直接用。</p>
                        </div>'''

new_card3 = '''                        <div class="bg-white border border-gray-200 rounded-2xl p-6 hover:shadow-lg hover:-translate-y-1 transition-all duration-300">
                            <div class="w-14 h-14 bg-gradient-to-br from-gray-800 to-gray-900 rounded-full flex items-center justify-center mb-5 shadow-lg">
                                <span class="text-white text-2xl font-bold">3</span>
                            </div>
                            <h4 class="text-lg font-bold text-gray-900 mb-2">直接拿去用</h4>
                            <p class="text-gray-500 text-sm leading-relaxed">一键复制，拜访前 5 分钟就能准备好，直接用。</p>
                        </div>'''

# 把 lines 转成字符串来替换
content = ''.join(lines)

content = content.replace(old_card1, new_card1)
content = content.replace(old_card2, new_card2)
content = content.replace(old_card3, new_card3)

# 保存
with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ 已更新三步上手样式")
print("  - 方形数字 → 圆形渐变数字 + 阴影")
print("  - 圆角加大（rounded-xl → rounded-2xl）")
print("  - 悬浮效果：向上移动 + 阴影加深")
print("  - 标题字号加大")
print("  - 行高优化")
