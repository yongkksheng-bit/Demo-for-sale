with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 旧的三步上手卡片
old_step1 = '''                        <div class="bg-white border border-gray-200 rounded-xl p-6 hover:shadow-lg transition-shadow">
                            <div class="w-12 h-12 bg-gray-900 rounded-lg flex items-center justify-center mb-4">
                                <span class="text-white text-xl font-bold">1</span>
                            </div>
                            <h4 class="font-bold text-gray-900 mb-2">输入客户信息</h4>
                            <p class="text-gray-500 text-sm">填写公司名称、行业、拜访对象。不知道也没关系，公司名就够了。</p>
                        </div>'''

old_step2 = '''                        <div class="bg-white border border-gray-200 rounded-xl p-6 hover:shadow-lg transition-shadow">
                            <div class="w-12 h-12 bg-gray-900 rounded-lg flex items-center justify-center mb-4">
                                <span class="text-white text-xl font-bold">2</span>
                            </div>
                            <h4 class="font-bold text-gray-900 mb-2">AI 一键生成</h4>
                            <p class="text-gray-500 text-sm">点击生成按钮，AI 自动分析，30 秒出结果，不用等。</p>
                        </div>'''

old_step3 = '''                        <div class="bg-white border border-gray-200 rounded-xl p-6 hover:shadow-lg transition-shadow">
                            <div class="w-12 h-12 bg-gray-900 rounded-lg flex items-center justify-center mb-4">
                                <span class="text-white text-xl font-bold">3</span>
                            </div>
                            <h4 class="font-bold text-gray-900 mb-2">直接拿去用</h4>
                            <p class="text-gray-500 text-sm">一键复制，拜访前 5 分钟就能准备好，直接用。</p>
                        </div>'''

# 新的三步上手卡片：圆形渐变数字 + 悬浮效果 + 加大圆角
new_step1 = '''                        <div class="bg-white border border-gray-200 rounded-2xl p-6 hover:-translate-y-1 hover:shadow-lg transition-all duration-300">
                            <div class="w-12 h-12 bg-gradient-to-br from-gray-800 to-gray-900 rounded-full flex items-center justify-center mb-4 shadow-md">
                                <span class="text-white text-xl font-bold">1</span>
                            </div>
                            <h4 class="font-bold text-gray-900 text-lg mb-2">输入客户信息</h4>
                            <p class="text-gray-500 leading-relaxed">填写公司名称、行业、拜访对象。不知道也没关系，公司名就够了。</p>
                        </div>'''

new_step2 = '''                        <div class="bg-white border border-gray-200 rounded-2xl p-6 hover:-translate-y-1 hover:shadow-lg transition-all duration-300">
                            <div class="w-12 h-12 bg-gradient-to-br from-gray-800 to-gray-900 rounded-full flex items-center justify-center mb-4 shadow-md">
                                <span class="text-white text-xl font-bold">2</span>
                            </div>
                            <h4 class="font-bold text-gray-900 text-lg mb-2">AI 一键生成</h4>
                            <p class="text-gray-500 leading-relaxed">点击生成按钮，AI 自动分析，30 秒出结果，不用等。</p>
                        </div>'''

new_step3 = '''                        <div class="bg-white border border-gray-200 rounded-2xl p-6 hover:-translate-y-1 hover:shadow-lg transition-all duration-300">
                            <div class="w-12 h-12 bg-gradient-to-br from-gray-800 to-gray-900 rounded-full flex items-center justify-center mb-4 shadow-md">
                                <span class="text-white text-xl font-bold">3</span>
                            </div>
                            <h4 class="font-bold text-gray-900 text-lg mb-2">直接拿去用</h4>
                            <p class="text-gray-500 leading-relaxed">一键复制，拜访前 5 分钟就能准备好，直接用。</p>
                        </div>'''

# 替换
count = 0
if old_step1 in content:
    content = content.replace(old_step1, new_step1)
    count += 1
if old_step2 in content:
    content = content.replace(old_step2, new_step2)
    count += 1
if old_step3 in content:
    content = content.replace(old_step3, new_step3)
    count += 1

# 保存
with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ 已更新 {count} 个三步上手卡片")
if count == 3:
    print("  - 方形数字 → 圆形渐变数字 + 阴影")
    print("  - 圆角加大（rounded-xl → rounded-2xl）")
    print("  - 悬浮效果：向上移动 + 阴影加深")
    print("  - 标题字号加大")
    print("  - 行高优化")
else:
    print("❌ 有些没匹配上")
