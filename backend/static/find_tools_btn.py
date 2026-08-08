with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找"销售工具箱"文字的位置
idx = content.find("销售工具箱")
if idx != -1:
    print(f"销售工具箱在第 {content[:idx].count(chr(10)) + 1} 行")
    
    # 往前找最近的 button 或者 a 标签
    btn_start = content.rfind("<button", 0, idx)
    a_start = content.rfind("<a", 0, idx)
    
    start = max(btn_start, a_start)
    if start != -1:
        end = content.find("</button>", idx)
        if end == -1:
            end = content.find("</a>", idx)
        end += len("</button>") if end != -1 else len("</a>")
        
        print("\n=== 销售工具箱按钮 ===")
        print(content[start:end])
else:
    print("❌ 找不到销售工具箱文字")
