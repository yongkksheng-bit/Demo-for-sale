with open("app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 第655行附近
print("第650-660行：")
for i in range(649, 660):
    if i < len(lines):
        print(f"  {i+1}: {lines[i].rstrip()[:80]}")
