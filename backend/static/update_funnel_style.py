with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 旧的 renderPipelineFunnel 函数
old_func_start = content.find("function renderPipelineFunnel() {")
old_func_end = content.find("}", old_func_start) + 1
old_func = content[old_func_start:old_func_end]

print("旧函数长度:", len(old_func))

# 新的 renderPipelineFunnel 函数
new_func = '''function renderPipelineFunnel() {
    const container = document.getElementById('pipeline-funnel');
    const maxCount = Math.max(...stageConfig.map(s => customers.filter(c => c.stage === s.key).length), 1);
    const totalCount = customers.length;
    
    container.innerHTML = stageConfig.map((stage, index) => {
        const stageCustomers = customers.filter(c => c.stage === stage.key);
        const count = stageCustomers.length;
        const amount = stageCustomers.reduce((sum, c) => sum + (c.amount || 0), 0);
        const percent = totalCount > 0 ? Math.round((count / totalCount) * 100) : 0;
        const widthPercent = Math.max((count / maxCount) * 100, 5);
        
        return `
            <div class="bg-white border border-gray-200 rounded-xl p-4 shadow-sm hover:shadow-md transition-shadow">
                <div class="flex items-center justify-between mb-2">
                    <div class="flex items-center space-x-3">
                        <span class="w-7 h-7 rounded-full bg-gray-100 text-gray-700 flex items-center justify-center text-sm font-semibold">${index + 1}</span>
                        <span class="font-medium text-gray-900">${stage.label}</span>
                    </div>
                    <div class="text-right">
                        <div class="text-lg font-bold text-gray-900">${count} <span class="text-sm font-normal text-gray-500">个</span></div>
                    </div>
                </div>
                <div class="flex items-center justify-between text-sm text-gray-500 mb-3">
                    <span>预计金额</span>
                    <span class="font-medium text-gray-700">${amount.toFixed(1)} 万</span>
                </div>
                <div class="w-full h-2 bg-gray-100 rounded-full overflow-hidden">
                    <div class="h-full bg-gray-400 rounded-full transition-all duration-300" style="width: ${widthPercent}%"></div>
                </div>
                <div class="flex items-center justify-between text-xs text-gray-400 mt-2">
                    <span>占比 ${percent}%</span>
                    <span>成交概率 ${stage.probability}%</span>
                </div>
            </div>
        `;
    }).join('');
}'''

# 替换
content = content.replace(old_func, new_func)

with open("app.js", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ 已重写 renderPipelineFunnel 函数")
print("  从彩色横向条形图 → 垂直卡片式")
print("  白色背景 + 灰色边框 + 阴影")
print("  黑白简约风格")
