with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 统计替换次数
count = 0

# 1. 侧边栏底部的身份图标（w-8 h-8）
old_sidebar_icon = '''                    <div class="w-8 h-8 rounded-full bg-gray-900 flex items-center justify-center flex-shrink-0">
                        <i class="fa fa-briefcase text-white text-xs"></i>
                    </div>'''

new_sidebar_icon = '''                    <div class="w-8 h-8 rounded-full bg-gray-900 flex items-center justify-center flex-shrink-0">
                        <i class="fa fa-user text-white text-xs"></i>
                    </div>'''

if old_sidebar_icon in content:
    content = content.replace(old_sidebar_icon, new_sidebar_icon)
    count += 1
    print("✅ 侧边栏身份图标已换成用户图标")

# 2. 首页 hero 区域的身份按钮图标
# 先找找
idx = content.find("选择身份")
if idx != -1:
    # 往前找图标
    area = content[idx-200:idx+200]
    if "fa-briefcase" in area:
        print("\n首页也有公文包图标，需要替换")
        # 找具体的代码
        import re
        # 找 fa-briefcase 附近的 div
        brief_idx = content.find("fa-briefcase", idx-200)
        if brief_idx != -1:
            # 往前找 div 开始
            div_start = content.rfind("<div", 0, brief_idx)
            # 往后找 div 结束
            div_end = content.find("</div>", brief_idx) + 6
            old_icon = content[div_start:div_end]
            print(f"首页图标代码: {old_icon[:100]}...")
            
            # 替换 fa-briefcase → fa-user
            new_icon = old_icon.replace("fa-briefcase", "fa-user")
            content = content.replace(old_icon, new_icon)
            count += 1
            print("✅ 首页身份图标已换成用户图标")

# 3. 去掉 truncate，让文字可以换行（侧边栏）
content = content.replace(
    '<div class="text-sm font-medium text-gray-900 truncate" id="current-identity-name">',
    '<div class="text-sm font-medium text-gray-900 leading-tight" id="current-identity-name">'
)
print("✅ 侧边栏身份文字去掉 truncate，可以换行显示")

# 保存
with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print(f"\n总共替换了 {count} 个图标")
