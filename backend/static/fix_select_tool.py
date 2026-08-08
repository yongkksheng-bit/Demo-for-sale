with open("app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找到 selectTool 函数开始的行
start_line = -1
for i, line in enumerate(lines):
    if "function selectTool" in line:
        start_line = i
        break

if start_line == -1:
    print("❌ 找不到 selectTool 函数")
else:
    print(f"selectTool 函数从第 {start_line+1} 行开始")
    
    # 找到函数结束的行（统计大括号）
    brace_count = 0
    end_line = -1
    for i in range(start_line, len(lines)):
        brace_count += lines[i].count("{")
        brace_count -= lines[i].count("}")
        if brace_count == 0 and i > start_line:
            end_line = i
            break
    
    if end_line != -1:
        print(f"selectTool 函数到第 {end_line+1} 行结束")
        
        # 替换
        new_func_lines = [
            "function selectTool(toolName) {\n",
            "    // 切换右侧内容\n",
            "    document.querySelectorAll('.tool-content').forEach(function(el) {\n",
            "        el.classList.add('hidden');\n",
            "    });\n",
            "    \n",
            "    var activeContent = document.getElementById('tool-content-' + toolName);\n",
            "    if (activeContent) {\n",
            "        activeContent.classList.remove('hidden');\n",
            "    }\n",
            "    \n",
            "    // 更新左侧导航选中状态\n",
            "    document.querySelectorAll('.tool-nav-btn').forEach(function(btn) {\n",
            "        btn.style.backgroundColor = '';\n",
            "        btn.style.color = '';\n",
            "    });\n",
            "    \n",
            "    var activeBtn = document.getElementById('tool-' + toolName);\n",
            "    if (activeBtn) {\n",
            "        activeBtn.style.backgroundColor = '#111827';\n",
            "        activeBtn.style.color = 'white';\n",
            "    }\n",
            "    \n",
            "    // 如果是ROI计算器，重新计算一下\n",
            "    if (toolName === 'roi') {\n",
            "        calculateROI();\n",
            "    }\n",
            "}\n",
        ]
        
        # 找到注释行
        comment_line = -1
        for i in range(start_line - 5, start_line):
            if "销售工具箱切换" in lines[i]:
                comment_line = i
                break
        
        if comment_line != -1:
            # 从注释行开始替换
            new_lines = lines[:comment_line] + ["// ========== 销售工具箱切换 ==========\n"] + new_func_lines + lines[end_line+1:]
        else:
            new_lines = lines[:start_line] + new_func_lines + lines[end_line+1:]
        
        with open("app.js", "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        
        print("✅ selectTool 函数已完整替换")
    else:
        print("❌ 找不到函数结束")
