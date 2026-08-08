with open("app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 第862行（索引861）多了一个}，删掉它
# 先确认一下
print(f"第861行: {lines[860].strip()}")
print(f"第862行: {lines[861].strip()}")
print(f"第863行: {lines[862].strip()}")

# 删掉第862行（索引861）
if lines[861].strip() == "}":
    del lines[861]
    with open("app.js", "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("删掉了多余的}")
else:
    print("第862行不是}，检查一下")
