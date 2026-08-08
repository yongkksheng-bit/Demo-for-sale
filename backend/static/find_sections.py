with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. 找"三步上手"或"输入客户信息"
idx1 = content.find("输入客户信息")
if idx1 != -1:
    # 往前找section开始
    section_start = content.rfind("<section", 0, idx1)
    print(f"=== 三步上手部分 ===")
    print(f"开始位置: {section_start}")
    print(f"前200字: {content[section_start:section_start+200]}...")

# 2. 找方案生成的步骤指示器
idx2 = content.find("你卖什么？")
if idx2 != -1:
    print(f"\n=== 方案生成步骤 ===")
    print(f"位置: {idx2}")
    # 前后各100字
    print(f"上下文: ...{content[idx2-100:idx2+100]}...")

# 3. 找销售工具箱的标题
idx3 = content.find('id="tools"')
if idx3 != -1:
    print(f"\n=== 销售工具箱 ===")
    print(f"开始位置: {idx3}")
    print(f"前300字: {content[idx3:idx3+300]}...")
