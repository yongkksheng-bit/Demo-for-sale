with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. 把公文包图标换成用户图标
# 先找侧边栏底部的身份图标
# 往前找更多，找到图标
idx = content.find("点击切换身份")
if idx != -1:
    # 往前找更多
    start = content.rfind("<button", 0, idx)
    area = content[start:start+600]
    print("=== 身份按钮完整代码 ===")
    print(area)
    
    # 替换图标：fa-briefcase → fa-user
    # 先看看有没有 fa-briefcase
    if "fa-briefcase" in area:
        print("\n找到 fa-briefcase 图标")
        # 替换
        content = content.replace(
            '<div class="w-10 h-10 rounded-full bg-gray-900 flex items-center justify-center mr-3 flex-shrink-0">\n                                <i class="fa fa-briefcase text-white text-sm"></i>\n                            </div>',
            '<div class="w-10 h-10 rounded-full bg-gray-900 flex items-center justify-center mr-3 flex-shrink-0">\n                                <i class="fa fa-user text-white text-sm"></i>\n                            </div>'
        )
        print("✅ 已换成用户图标")
    else:
        print("\n没找到 fa-briefcase，看看实际的图标类")
        # 找 i 标签
        import re
        match = re.search(r'<i class="fa fa-([^"]*)"', area)
        if match:
            print(f"实际图标: fa-{match.group(1)}")

# 2. 去掉 truncate，让文字可以换行
content = content.replace(
    '<div class="text-sm font-medium text-gray-900 truncate" id="current-identity-name">',
    '<div class="text-sm font-medium text-gray-900 leading-tight" id="current-identity-name">'
)

# 保存
with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("\n✅ 已修改身份显示区域")
print("  - 公文包图标 → 用户图标")
print("  - 去掉 truncate，文字可以换行显示完整")
