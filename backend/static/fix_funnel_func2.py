with open("app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 先看看第655行现在是什么
print(f"修改前第655行: {lines[654].rstrip()}")

# 第655行是 "}</div>"，把它改成 "}"
lines[654] = "}\n"

# 删掉第656行到第666行（索引655到665），这些都是旧函数的残留
del lines[655:666]

print(f"删除后剩余 {len(lines)} 行")

# 保存
with open("app.js", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("已保存")

# 再检查语法
import subprocess
result = subprocess.run(["node", "--check", "app.js"], capture_output=True, text=True)
if result.returncode == 0:
    print("✅ JS语法检查通过！")
else:
    print("❌ JS语法错误：")
    print(result.stderr[:500])
