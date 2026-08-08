with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 旧的销售工具箱开头
old_tools_header = '''        <section id="tools" class="section hidden py-8">
            <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-10">
                    <h2 class="text-2xl font-bold text-gray-900 mb-2">销售工具箱</h2>
                    <p class="text-gray-500 text-sm">助力销售全流程，提升成单效率</p>
                </div>'''

# 新的销售工具箱开头（和其他模块一致）
new_tools_header = '''        <section id="tools" class="section hidden py-16">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-12">
                    <h2 class="text-3xl font-bold text-gray-900 mb-4">销售工具箱</h2>
                    <p class="text-gray-600">助力销售全流程，提升成单效率</p>
                </div>'''

if old_tools_header in content:
    content = content.replace(old_tools_header, new_tools_header)
    print("✅ 已更新销售工具箱头部布局")
    print("  - py-8 → py-16（上下间距加大）")
    print("  - max-w-6xl → max-w-7xl（宽度加大）")
    print("  - mb-10 → mb-12（底部间距加大）")
    print("  - text-2xl → text-3xl（标题字号加大）")
    print("  - text-gray-500 text-sm → text-gray-600（副标题样式统一）")
else:
    print("❌ 没找到旧的销售工具箱头部")
    # 看看实际的
    idx = content.find('id="tools"')
    print(f"\n实际内容：{content[idx:idx+300]}")

# 保存
with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
