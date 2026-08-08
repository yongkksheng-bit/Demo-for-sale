with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 检查方案生成按钮
if 'bg-white border border-gray-200' in content and 'generateSolution' in content:
    print("✅ 方案生成按钮已改成白色样式")
else:
    print("❌ 方案生成按钮没改对")

# 检查客户背调生成按钮
if 'bg-white border border-gray-200' in content and 'generateResearch' in content:
    print("✅ 客户背调生成按钮已改成白色样式")
else:
    print("❌ 客户背调生成按钮没改对")

# 检查结果卡片
if 'bg-white border border-gray-200 rounded-xl p-6 shadow-sm' in content:
    print("✅ 结果区域卡片已改成带边框阴影的白色样式")
else:
    print("❌ 结果区域卡片没改对")
