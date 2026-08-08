with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. 修改模态框的内层div，改成flex布局
# 原来的：<div class="bg-white rounded-2xl w-full max-w-lg max-h-[80vh] overflow-hidden">
# 改成：<div class="bg-white rounded-2xl w-full max-w-lg max-h-[80vh] overflow-hidden flex flex-col">
old_modal_inner = '<div class="bg-white rounded-2xl w-full max-w-lg max-h-[80vh] overflow-hidden">'
new_modal_inner = '<div class="bg-white rounded-2xl w-full max-w-lg max-h-[80vh] overflow-hidden flex flex-col">'
content = content.replace(old_modal_inner, new_modal_inner, 1)

# 2. 修改内容区域，改成 flex-1
# 原来的：<div class="p-6 overflow-y-auto max-h-[65vh]">
# 改成：<div class="p-6 overflow-y-auto flex-1">
old_content = '<div class="p-6 overflow-y-auto max-h-[65vh]">'
new_content = '<div class="p-6 overflow-y-auto flex-1">'
content = content.replace(old_content, new_content, 1)

# 3. 底部确认按钮区域加上 flex-shrink-0
old_footer = '<div class="p-6 border-t border-gray-200">'
new_footer = '<div class="p-6 border-t border-gray-200 flex-shrink-0">'
content = content.replace(old_footer, new_footer, 1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ 模态框已改为flex布局，确认按钮永远固定在底部")
