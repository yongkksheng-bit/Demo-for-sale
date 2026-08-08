with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 在文件末尾添加 selectTool 函数
select_tool_func = '''

// ========== 销售工具箱切换 ==========
function selectTool(toolName) {
    // 更新左侧导航选中状态
    document.querySelectorAll('.tool-nav-btn').forEach(btn => {
        btn.classList.remove('bg-gray-900', 'text-white');
        btn.classList.add('hover:bg-gray-50');
        btn.querySelector('i').classList.remove('text-white');
        btn.querySelector('i').classList.add('text-gray-400');
        btn.querySelector('.font-medium').classList.remove('text-white');
        btn.querySelector('.font-medium').classList.add('text-gray-900');
        btn.querySelector('.text-xs').classList.remove('text-gray-300');
        btn.querySelector('.text-xs').classList.add('text-gray-400');
    });
    
    const activeBtn = document.getElementById('tool-' + toolName);
    if (activeBtn) {
        activeBtn.classList.add('bg-gray-900', 'text-white');
        activeBtn.classList.remove('hover:bg-gray-50');
        activeBtn.querySelector('i').classList.add('text-white');
        activeBtn.querySelector('i').classList.remove('text-gray-400');
        activeBtn.querySelector('.font-medium').classList.add('text-white');
        activeBtn.querySelector('.font-medium').classList.remove('text-gray-900');
        activeBtn.querySelector('.text-xs').classList.add('text-gray-300');
        activeBtn.querySelector('.text-xs').classList.remove('text-gray-400');
    }
    
    // 切换右侧内容
    document.querySelectorAll('.tool-content').forEach(content => {
        content.classList.add('hidden');
    });
    
    const activeContent = document.getElementById('tool-content-' + toolName);
    if (activeContent) {
        activeContent.classList.remove('hidden');
    }
    
    // 如果是ROI计算器，重新计算一下
    if (toolName === 'roi') {
        calculateROI();
    }
}
'''

content += select_tool_func

with open("app.js", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ selectTool 函数已添加")
