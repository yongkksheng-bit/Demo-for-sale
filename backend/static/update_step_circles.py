with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 替换激活状态的步骤圆圈
# 原来的：bg-gray-900 text-white
# 改成：bg-white border border-gray-200 text-gray-900 shadow-sm
old_active = 'w-8 h-8 rounded-full bg-gray-900 text-white flex items-center justify-center text-sm font-semibold'
new_active = 'w-8 h-8 rounded-full bg-white border border-gray-200 text-gray-900 flex items-center justify-center text-sm font-semibold shadow-sm'

# 统计替换次数
count = content.count(old_active)
content = content.replace(old_active, new_active)

print(f"✅ 已修改 {count} 个激活状态的步骤圆圈")
print("  从：黑底白字")
print("  改成：白底黑字 + 灰色边框 + 阴影")

# 未激活的保持灰色，不用改

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
