with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 检查工具导航按钮
print("=== 工具导航按钮 ===")
import re
buttons = re.findall(r'<button[^>]*onclick="selectTool\(([^)]+)\)"[^>]*id="([^"]+)"[^>]*>', content)
for btn in buttons:
    print(f"  onclick: selectTool({btn[0]}), id: {btn[1]}")

# 检查工具内容区
print("\n=== 工具内容区 ===")
contents = re.findall(r'<div[^>]*id="(tool-content-[^"]+)"[^>]*class="([^"]*)"[^>]*>', content)
for c in contents:
    print(f"  id: {c[0]}, class: {c[1][:50]}...")

# 检查第一个工具是不是默认显示的
print("\n=== 默认显示检查 ===")
if 'id="tool-content-script" class="tool-content"' in content:
    print("✅ 销售话术默认显示")
else:
    print("❌ 销售话术不是默认显示（可能有hidden类）")
