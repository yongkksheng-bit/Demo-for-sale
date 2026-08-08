with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找到确认按钮的位置
confirm_btn_idx = content.find('id="confirm-identity-btn"')
if confirm_btn_idx != -1:
    # 往前找按钮开始
    btn_start = content.rfind("<button", 0, confirm_btn_idx)
    # 往后找按钮结束
    btn_end = content.find("</button>", confirm_btn_idx) + len("</button>")
    
    print("=== 确认按钮 ===")
    print(content[btn_start:btn_end])
    
    # 看看确认按钮在哪个div里
    # 往前找最近的 <div
    div_start = content.rfind("<div", 0, btn_start)
    print(f"\n确认按钮所在div开始: {content[div_start:div_start+100]}")
