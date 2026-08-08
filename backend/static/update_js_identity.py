with open("app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找到身份选择相关函数的位置
start_line = -1
end_line = -1

for i, line in enumerate(lines):
    if "// ========== 身份选择 ==========" in line:
        start_line = i
    if start_line != -1 and "function loadIdentity" in line:
        # 找到 loadIdentity 函数的结束
        for j in range(i, min(i+20, len(lines))):
            if lines[j].strip() == "}" and j > i:
                end_line = j
                break
        break

print(f"身份选择函数从第{start_line+1}行到第{end_line+1}行")

# 新的身份选择逻辑
new_functions = '''// ========== 身份选择 ==========
let selectedIndustry = "";
let selectedSalesType = "";

function showIdentityModal() {
    document.getElementById('identity-modal').classList.remove('hidden');
    // 重置选中状态
    selectedIndustry = "";
    selectedSalesType = "";
    updateIdentitySelectionUI();
}

function hideIdentityModal() {
    document.getElementById('identity-modal').classList.add('hidden');
}

function selectIndustry(industry) {
    selectedIndustry = industry;
    updateIdentitySelectionUI();
}

function selectSalesType(salesType) {
    selectedSalesType = salesType;
    updateIdentitySelectionUI();
}

function updateIdentitySelectionUI() {
    // 更新行业选中状态
    document.querySelectorAll('.industry-option').forEach(btn => {
        btn.classList.remove('border-gray-900', 'bg-gray-50');
        btn.classList.add('border-gray-200');
    });
    if (selectedIndustry) {
        document.querySelectorAll('.industry-option').forEach(btn => {
            if (btn.textContent.includes(selectedIndustry)) {
                btn.classList.remove('border-gray-200');
                btn.classList.add('border-gray-900', 'bg-gray-50');
            }
        });
        // 解锁第二步
        const salesTypeSection = document.getElementById('sales-type-section');
        if (salesTypeSection) {
            salesTypeSection.classList.remove('opacity-50', 'pointer-events-none');
        }
        const step2Badge = document.getElementById('step2-badge');
        if (step2Badge) {
            step2Badge.classList.remove('bg-gray-300');
            step2Badge.classList.add('bg-gray-900');
        }
    }
    
    // 更新销售类型选中状态
    document.querySelectorAll('.sales-type-option').forEach(btn => {
        btn.classList.remove('border-gray-900', 'bg-gray-50');
        btn.classList.add('border-gray-200');
    });
    if (selectedSalesType) {
        document.querySelectorAll('.sales-type-option').forEach(btn => {
            if (btn.textContent.includes(selectedSalesType)) {
                btn.classList.remove('border-gray-200');
                btn.classList.add('border-gray-900', 'bg-gray-50');
            }
        });
    }
    
    // 更新确认按钮状态
    const confirmBtn = document.getElementById('confirm-identity-btn');
    if (confirmBtn) {
        if (selectedIndustry && selectedSalesType) {
            confirmBtn.disabled = false;
            confirmBtn.classList.remove('bg-gray-300', 'cursor-not-allowed');
            confirmBtn.classList.add('bg-gray-900', 'hover:bg-gray-800', 'cursor-pointer');
            confirmBtn.textContent = `确认：${selectedIndustry} · ${selectedSalesType}`;
        } else {
            confirmBtn.disabled = true;
            confirmBtn.classList.add('bg-gray-300', 'cursor-not-allowed');
            confirmBtn.classList.remove('bg-gray-900', 'hover:bg-gray-800', 'cursor-pointer');
            if (!selectedIndustry) {
                confirmBtn.textContent = "请先选择行业";
            } else {
                confirmBtn.textContent = "请选择销售类型";
            }
        }
    }
}

function confirmIdentity() {
    if (!selectedIndustry || !selectedSalesType) return;
    
    const identity = `${selectedIndustry} · ${selectedSalesType}`;
    currentIdentity = identity;
    localStorage.setItem('xiaoshouyi_identity', identity);
    
    // 更新显示
    updateIdentityDisplay(identity);
    
    hideIdentityModal();
}

function updateIdentityDisplay(identity) {
    // 更新侧边栏底部
    const sidebarIdentity = document.getElementById('current-identity-name');
    if (sidebarIdentity) {
        sidebarIdentity.textContent = identity;
    }
    
    // 更新首页选择身份按钮
    const heroIdentityBtn = document.getElementById('hero-identity-text');
    if (heroIdentityBtn) {
        heroIdentityBtn.textContent = identity;
    }
}

function loadIdentity() {
    const saved = localStorage.getItem('xiaoshouyi_identity');
    if (saved) {
        currentIdentity = saved;
        updateIdentityDisplay(saved);
    }
}
'''

# 替换
new_lines = lines[:start_line] + [new_functions] + lines[end_line+1:]

with open("app.js", "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("JS身份选择逻辑更新完成！")
