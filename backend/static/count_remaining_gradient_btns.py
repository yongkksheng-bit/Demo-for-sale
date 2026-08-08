with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

import re

# 找所有渐变按钮
gradient_btns = re.findall(r'<button[^>]*bg-gradient-primary[^>]*>', content)
print(f"全站剩余渐变按钮数量: {len(gradient_btns)}")

# 看看都在哪些页面附近
pages = ["首页", "客户背调", "方案生成", "销售看板", "客户管理", "智能对话", "销售工具箱"]
for page in pages:
    idx = content.find(page)
    if idx != -1:
        # 在附近找渐变按钮
        search_area = content[idx:idx + 3000]
        count = len(re.findall(r'<button[^>]*bg-gradient-primary[^>]*>', search_area))
        if count > 0:
            print(f"  {page} 附近: {count} 个")
