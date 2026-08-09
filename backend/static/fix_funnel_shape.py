with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 找 renderPipelineFunnel 函数
idx = content.find("function renderPipelineFunnel")
if idx != -1:
    # 找到函数结束位置（找下一个 function 或者文件末尾）
    next_func = content.find("\nfunction ", idx + 10)
    if next_func == -1:
        end_idx = len(content)
    else:
        end_idx = next_func
    
    old_func = content[idx:end_idx]
    print("=== 旧的 renderPipelineFunnel 函数 ===")
    print(old_func[:500])
    
    # 新的漏斗函数：真正的漏斗形状，上宽下窄
    new_func = '''function renderPipelineFunnel() {
    const funnelEl = document.getElementById('pipeline-funnel');
    if (!funnelEl) return;
    
    const stages = [
        { key: 'lead', name: '潜在客户', color: 'gray', probability: 10 },
        { key: 'contact', name: '初步接触', color: 'blue', probability: 20 },
        { key: 'requirement', name: '需求确认', color: 'cyan', probability: 40 },
        { key: 'proposal', name: '方案沟通', color: 'purple', probability: 60 },
        { key: 'negotiation', name: '商务谈判', color: 'orange', probability: 80 },
        { key: 'won', name: '签约成交', color: 'green', probability: 100 },
    ];
    
    // 计算每个阶段的客户数和金额
    const stageData = stages.map(stage => {
        const stageCustomers = customers.filter(c => c.stage === stage.key);
        const count = stageCustomers.length;
        const amount = stageCustomers.reduce((sum, c) => sum + (c.amount || 0), 0);
        return { ...stage, count, amount };
    });
    
    const totalCount = stageData.reduce((sum, s) => sum + s.count, 0);
    const totalAmount = stageData.reduce((sum, s) => sum + s.amount, 0);
    
    // 漏斗宽度比例：从100%到40%，每个阶段递减
    const widthPercentages = [100, 90, 80, 70, 60, 50];
    
    let html = '<div class="space-y-2">';
    
    stageData.forEach((stage, index) => {
        const widthPct = widthPercentages[index];
        const percentage = totalCount > 0 ? ((stage.count / totalCount) * 100).toFixed(0) : 0;
        
        html += `
            <div class="flex justify-center">
                <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-4 transition-all hover:shadow-md" 
                     style="width: ${widthPct}%; min-width: 280px;">
                    <div class="flex items-center justify-between mb-2">
                        <div class="flex items-center">
                            <div class="w-7 h-7 rounded-full bg-gray-100 flex items-center justify-center text-sm font-bold text-gray-600 mr-3">
                                ${index + 1}
                            </div>
                            <span class="font-semibold text-gray-900">${stage.name}</span>
                        </div>
                        <div class="text-right">
                            <div class="font-bold text-gray-900">${stage.count} 个</div>
                        </div>
                    </div>
                    <div class="text-sm text-gray-500 mb-2">预计金额：${stage.amount.toFixed(1)} 万</div>
                    <div class="w-full bg-gray-100 rounded-full h-1.5 mb-1">
                        <div class="bg-gray-400 h-1.5 rounded-full" style="width: ${percentage}%"></div>
                    </div>
                    <div class="flex justify-between text-xs text-gray-400">
                        <span>占比 ${percentage}%</span>
                        <span>成交概率 ${stage.probability}%</span>
                    </div>
                </div>
            </div>
        `;
    });
    
    html += '</div>';
    
    funnelEl.innerHTML = html;
}'''
    
    content = content[:idx] + new_func + content[end_idx:]
    
    # 保存
    with open("app.js", "w", encoding="utf-8") as f:
        f.write(content)
    
    print("\n✅ 已更新销售漏斗为真正的漏斗形状（上宽下窄）")
else:
    print("❌ 没找到 renderPipelineFunnel 函数")
