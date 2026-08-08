with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 找到原来的 selectTool 函数，替换成简化版
old_func_start = content.find("// ========== 销售工具箱切换 ==========")
old_func_end = content.find("}", content.find("function selectTool", old_func_start)) + 1

old_func = content[old_func_start:old_func_end]

new_func = '''// ========== 销售工具箱切换 ==========
function selectTool(toolName) {
    // 切换右侧内容
    document.querySelectorAll('.tool-content').forEach(function(el) {
        el.classList.add('hidden');
    });
    
    var activeContent = document.getElementById('tool-content-' + toolName);
    if (activeContent) {
        activeContent.classList.remove('hidden');
    }
    
    // 更新左侧导航选中状态
    document.querySelectorAll('.tool-nav-btn').forEach(function(btn) {
        btn.style.backgroundColor = '';
        btn.style.color = '';
    });
    
    var activeBtn = document.getElementById('tool-' + toolName);
    if (activeBtn) {
        activeBtn.style.backgroundColor = '#111827';
        activeBtn.style.color = 'white';
    }
    
    // 如果是ROI计算器，重新计算一下
    if (toolName === 'roi') {
        calculateROI();
    }
}'''

content = content.replace(old_func, new_func)

with open("app.js", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ selectTool 函数已简化，用style直接改样式，避免querySelector报错")
