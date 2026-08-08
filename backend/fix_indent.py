with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

# 修复缩进问题
old_line = "from services.bid_service import bid_analysis_service"
new_line = "    from services.bid_service import bid_analysis_service"
content = content.replace(old_line, new_line, 1)

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)

print("缩进修复完成！")
