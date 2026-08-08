with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找所有包含 bg-gradient-primary 的行
for i, line in enumerate(lines):
    if "bg-gradient-primary" in line:
        print(f"第 {i+1} 行: {line.strip()[:100]}...")
