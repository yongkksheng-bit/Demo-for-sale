with open("app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找到 selectTool 函数
start = -1
for i, line in enumerate(lines):
    if "function selectTool" in line:
        start = i
        break

if start != -1:
    # 找函数结束
    brace_count = 0
    end = -1
    for i in range(start, len(lines)):
        brace_count += lines[i].count("{")
        brace_count -= lines[i].count("}")
        if brace_count == 0 and i > start:
            end = i
            break
    
    if end != -1:
        # 替换函数
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
            "        btn.style.fontWeight = '';\n",
            "    });\n",
            "    \n",
            "    var activeBtn = document.getElementById('tool-' + toolName);\n",
            "    if (activeBtn) {\n",
            "        activeBtn.style.backgroundColor = '#e5e7eb';\n",
            "        activeBtn.style.fontWeight = '600';\n",
            "    }\n",
            "    \n",
            "    // 如果是ROI计算器，重新计算一下\n",
            "    if (toolName === 'roi') {\n",
            "        calculateROI();\n",
            "    }\n",
            "}\n",
        ]
        
        new_lines = lines[:start] + new_func_lines + lines[end+1:]
        
        with open("app.js", "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        
        print("✅ selectTool 函数已更新，选中状态改为灰色背景+加粗字体")
