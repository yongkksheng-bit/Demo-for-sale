with open("app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 第822行（索引821）现在有两个引号，删掉一个
line = lines[821]
print(f"当前: {line.rstrip()}")

# 把 ""; 改成 ";
if '"";' in line:
    new_line = line.replace('"";', '";')
    lines[821] = new_line
    print(f"恢复后: {new_line.rstrip()}")

with open("app.js", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("\n✅ 已恢复")
