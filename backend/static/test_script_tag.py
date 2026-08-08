with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找到所有的 script 标签
import re
scripts = re.findall(r'<script[^>]*src="([^"]*)"[^>]*>', content)
print("=== 脚本文件 ===")
for s in scripts:
    print(f"  - {s}")

# 看看 app.js 的位置
idx = content.find("app.js")
if idx != -1:
    # 往前找 script 标签
    script_start = content.rfind("<script", 0, idx)
    script_end = content.find(">", idx) + 1
    print(f"\n=== app.js 脚本标签 ===")
    print(content[script_start:script_end])
    
    # 看看是在 body 里还是 head 里
    head_end = content.find("</head>")
    body_start = content.find("<body")
    if idx < head_end:
        print("\n脚本在 head 里")
    elif idx > body_start:
        print("\n脚本在 body 里")
