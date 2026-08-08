with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 找到 renderPipelineFunnel 函数的开始
func_start = content.find("function renderPipelineFunnel() {")
print(f"函数开始位置: {func_start}")

# 找到函数的结束位置（匹配大括号）
brace_count = 0
func_end = -1
for i in range(func_start, len(content)):
    if content[i] == '{':
        brace_count += 1
    elif content[i] == '}':
        brace_count -= 1
        if brace_count == 0:
            func_end = i + 1
            break

print(f"函数结束位置: {func_end}")
print(f"函数长度: {func_end - func_start} 字符")

# 提取旧函数
old_func = content[func_start:func_end]
print(f"\n旧函数前100字: {old_func[:100]}...")
print(f"旧函数后100字: ...{old_func[-100:]}")

# 新函数
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
new_content = content[:func_start] + new_func + content[func_end:]

# 保存
with open("app.js", "w", encoding="utf-8") as f:
    f.write(new_content)

print("\n✅ 已替换 renderPipelineFunnel 函数")

# 检查语法
import subprocess
result = subprocess.run(["node", "--check", "app.js"], capture_output=True, text=True)
if result.returncode == 0:
    print("✅ JS语法检查通过！")
else:
    print("❌ JS语法错误：")
    print(result.stderr[:500])
