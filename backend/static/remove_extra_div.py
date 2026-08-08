with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 第1214行（索引1213）是多余的 </div>
# 让我先确认一下
print("删除前，第1212-1216行：")
for i in range(1211, 1216):
    print(f"  {i+1}: {lines[i].rstrip()}")

# 删除第1214行（索引1213）
del lines[1213]

print("\n删除后，第1212-1216行：")
for i in range(1211, 1216):
    print(f"  {i+1}: {lines[i].rstrip()}")

with open("index.html", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("\n✅ 已删除方案生成里多余的 </div>")
