with open("app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找到新函数结束的位置，然后找到后面多余的代码开始的位置
# 新函数结束后，下一行应该是空行或者其他代码
# 我们找到第二个 "function selectTool" 或者第二个 activeBtn.classList.add('bg-gray-900' 的位置

# 简单点：找到所有包含 "activeBtn.classList.add('bg-gray-900'" 的行
bg_gray_lines = []
for i, line in enumerate(lines):
    if "activeBtn.classList.add('bg-gray-900'" in line:
        bg_gray_lines.append(i)

print(f"找到 {len(bg_gray_lines)} 处 bg-gray-900 的代码")

if len(bg_gray_lines) > 1:
    # 第二个开始是多余的，往前找到函数开始，往后找到函数结束
    # 简单点：从第一个多余的行开始，到第2116行，都删掉
    # 先找到新函数结束的位置
    # 新函数里没有 querySelector，所以找到 "activeBtn.style.backgroundColor = '#111827'" 那一行，就是新函数的结尾附近
    
    new_func_end = -1
    for i, line in enumerate(lines):
        if "activeBtn.style.backgroundColor = '#111827'" in line:
            # 往后找函数结束
            brace_count = 0
            for j in range(i, len(lines)):
                brace_count += lines[j].count("{")
                brace_count -= lines[j].count("}")
                if brace_count == 0 and j > i:
                    new_func_end = j
                    break
            break
    
    if new_func_end != -1:
        print(f"新函数在第 {new_func_end+1} 行结束")
        
        # 找到后面多余代码的结束位置（第二个函数结束的位置）
        old_func_end = -1
        for i in range(new_func_end + 1, len(lines)):
            if lines[i].strip() == "}" and i > new_func_end + 10:
                # 检查是不是函数结束
                # 简单点，直接删到第2116行
                old_func_end = i
                break
        
        # 直接删掉从 new_func_end+1 到 2116 行（索引2115）
        # 先确认一下
        print(f"准备删除第 {new_func_end+2} 行到第 2116 行")
        
        new_lines = lines[:new_func_end+1] + lines[2116:]
        
        with open("app.js", "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        
        print("✅ 多余代码已删除")
