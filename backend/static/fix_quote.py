with open("app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 第822行（索引821）有问题
line = lines[821]
print(f"修复前: {line.rstrip()}")

# 修复：在结尾加上引号
# 找到最后一个 ; 的位置
semicolon_idx = line.rfind(";")
if semicolon_idx != -1:
    # 在 ; 前面加上 "
    new_line = line[:semicolon_idx] + '"' + line[semicolon_idx:]
    lines[821] = new_line
    print(f"修复后: {new_line.rstrip()}")

with open("app.js", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("\n✅ 引号问题已修复！")
