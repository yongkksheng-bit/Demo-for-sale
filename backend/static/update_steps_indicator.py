with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 旧的步骤指示器
old_steps = '''                            <div class="flex items-center justify-between mb-6">
                                <div class="flex items-center">
                                    <div id="step1-dot" class="w-8 h-8 rounded-full bg-white border-2 border-gray-900 flex items-center justify-center text-sm font-semibold text-gray-900">1</div>
                                    <span class="ml-2 font-medium text-dark">你卖什么？</span>
                                </div>
                                <div class="flex-1 h-0.5 bg-gray-200 mx-2"></div>
                                <div class="flex items-center">
                                    <div id="step2-dot" class="w-8 h-8 rounded-full bg-gray-100 border-2 border-gray-200 flex items-center justify-center text-sm font-medium text-gray-400">2</div>
                                    <span class="ml-2 text-gray-500 text-sm">选择场景</span>
                                </div>
                                <div class="flex-1 h-0.5 bg-gray-200 mx-2"></div>
                                <div class="flex items-center">
                                    <div id="step3-dot" class="w-8 h-8 rounded-full bg-gray-100 border-2 border-gray-200 flex items-center justify-center text-sm font-medium text-gray-400">3</div>
                                    <span class="ml-2 text-gray-500 text-sm">生成方案</span>
                                </div>
                            </div>'''

# 新的步骤指示器：文字不换行，调整间距
new_steps = '''                            <div class="flex items-center justify-between mb-6">
                                <div class="flex items-center flex-shrink-0">
                                    <div id="step1-dot" class="w-7 h-7 rounded-full bg-white border-2 border-gray-900 flex items-center justify-center text-sm font-semibold text-gray-900 flex-shrink-0">1</div>
                                    <span class="ml-2 font-medium text-gray-900 text-sm whitespace-nowrap">你卖什么</span>
                                </div>
                                <div class="flex-1 h-0.5 bg-gray-200 mx-2"></div>
                                <div class="flex items-center flex-shrink-0">
                                    <div id="step2-dot" class="w-7 h-7 rounded-full bg-gray-100 border-2 border-gray-200 flex items-center justify-center text-sm font-medium text-gray-400 flex-shrink-0">2</div>
                                    <span class="ml-2 text-gray-500 text-sm whitespace-nowrap">选择场景</span>
                                </div>
                                <div class="flex-1 h-0.5 bg-gray-200 mx-2"></div>
                                <div class="flex items-center flex-shrink-0">
                                    <div id="step3-dot" class="w-7 h-7 rounded-full bg-gray-100 border-2 border-gray-200 flex items-center justify-center text-sm font-medium text-gray-400 flex-shrink-0">3</div>
                                    <span class="ml-2 text-gray-500 text-sm whitespace-nowrap">生成方案</span>
                                </div>
                            </div>'''

if old_steps in content:
    content = content.replace(old_steps, new_steps)
    print("✅ 已更新步骤指示器样式")
    print("  - 文字不换行（whitespace-nowrap）")
    print("  - 圆点稍微缩小（w-8 → w-7）")
    print("  - 去掉问号，节省空间")
    print("  - 加上 flex-shrink-0 防止压缩")
else:
    print("❌ 没找到旧的步骤指示器，可能样式不一样")
    # 看看实际的内容是什么
    idx = content.find("步骤指示器")
    print(f"\n步骤指示器位置: {idx}")
    print(f"实际内容：{content[idx:idx+800]}")

# 保存
with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
