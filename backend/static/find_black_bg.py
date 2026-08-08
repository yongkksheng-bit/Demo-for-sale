with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找包含 bg-gray-900 的行
print("=== 包含 bg-gray-900 的行 ===")
for i, line in enumerate(lines):
    if "bg-gray-900" in line:
        print(f"第 {i+1} 行: {line.strip()[:100]}...")

print(f"\n总共 {sum(1 for line in lines if 'bg-gray-900' in line)} 行")
