with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 找到原来的 calculateROI 函数
start = content.find("function calculateROI")
end = content.find("// 页面加载时计算一次", start)

old_func = content[start:end]

new_func = '''function calculateROI() {
    const people = parseFloat(document.getElementById('roi-team-size').value) || 0;
    const salary = parseFloat(document.getElementById('roi-salary').value) || 0;
    const efficiency = parseFloat(document.getElementById('roi-efficiency').value) || 0;
    const cost = parseFloat(document.getElementById('roi-cost').value) || 0;
    
    // 计算年节省成本（元）
    const yearlySaving = people * salary * 12 * efficiency / 100;
    
    // 投入成本（元转万元）
    const costWan = cost / 10000;
    
    // 年节省成本（万元）
    const yearlySavingWan = yearlySaving / 10000;
    
    // ROI
    const roi = cost > 0 ? ((yearlySaving - cost) / cost * 100) : 0;
    
    // 回报周期（月）
    const monthlySaving = yearlySaving / 12;
    const paybackPeriod = monthlySaving > 0 ? (cost / monthlySaving) : 0;
    
    // 更新显示
    document.getElementById('roi-savings').textContent = yearlySavingWan.toFixed(0) + ' 万';
    document.getElementById('roi-investment').textContent = costWan.toFixed(0) + ' 万';
    document.getElementById('roi-ratio').textContent = roi.toFixed(0) + '%';
    document.getElementById('roi-period').textContent = paybackPeriod.toFixed(1) + ' 个月';
}

'''

content = content.replace(old_func, new_func)

with open("app.js", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ calculateROI 函数已更新，使用新的元素 id")
