with open("app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 保留前2089行（第1行到第2089行，索引0到2088）
# 第2088行是函数结束，第2089行是空行
new_lines = lines[:2089]

with open("app.js", "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print(f"✅ 已删除多余代码，现在总行数: {len(new_lines)}")
