with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找侧边栏的销售工具箱按钮
sidebar_start = content.find("sidebar")
if sidebar_start == -1:
    sidebar_start = 0

sidebar_end = content.find("</div>", sidebar_start + 500)
sidebar_content = content[sidebar_start:sidebar_end]

# 找销售工具箱相关的
if "销售工具箱" in sidebar_content:
    idx = sidebar_content.find("销售工具箱")
    # 往前找按钮
    btn_start = sidebar_content.rfind("<button", 0, idx)
    btn_end = sidebar_content.find("</button>", idx) + len("</button>")
    print("=== 侧边栏销售工具箱按钮 ===")
    print(sidebar_content[btn_start:btn_end])
else:
    print("❌ 侧边栏里找不到销售工具箱")
    # 看看侧边栏有什么
    import re
    buttons = re.findall(r'<button[^>]*>(.*?)</button>', sidebar_content, re.DOTALL)
    print(f"\n侧边栏按钮: {len(buttons)} 个")
    for btn in buttons[:10]:
        print(f"  - {btn.strip()[:50]}")
