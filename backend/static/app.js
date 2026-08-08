/**
 * 火山引擎智能方案顾问 - 前端逻辑
 */

// ========== 配置 ==========
const API_BASE_URL = 'https://demo-for-sale.onrender.com/api/v1';

// ========== 状态 ==========
let selectedIndustry = null;
let selectedScenario = null;
let currentSolution = null;
let currentResearch = null;
let chatHistory = [];
let currentIdentity = '大客户销售'; // 当前销售身份

// ========== 客户管理状态 ==========
let customers = [];
let records = [];
let currentCustomerId = null;
let editingCustomerId = null;

// ========== 行业数据 ==========
const industries = [
    {
        name: '零售电商',
        icon: '🛒',
        scenarios: [
            '智能推荐与个性化营销',
            '用户增长与留存',
            '智能客服与对话机器人',
            '商品搜索优化',
            '供应链智能预测'
        ]
    },
    {
        name: '金融',
        icon: '💰',
        scenarios: [
            '智能风控与反欺诈',
            '智能投顾与财富管理',
            '智能客服与营销',
            '文档智能处理',
            '合规与监管科技'
        ]
    },
    {
        name: '制造',
        icon: '🏭',
        scenarios: [
            '工业质检与缺陷检测',
            '预测性维护',
            '生产流程优化',
            '供应链管理',
            '数字孪生与仿真'
        ]
    },
    {
        name: '汽车',
        icon: '🚗',
        scenarios: [
            '智能座舱与车载助手',
            '自动驾驶与车路协同',
            '用户运营与营销',
            '售后智能服务',
            '供应链数字化'
        ]
    },
    {
        name: '教育',
        icon: '📚',
        scenarios: [
            '智能教学与个性化学习',
            'AI 题库与智能批改',
            '智能客服与招生',
            '知识图谱构建',
            '在线教育质量提升'
        ]
    },
    {
        name: '医疗健康',
        icon: '🏥',
        scenarios: [
            '医疗影像智能分析',
            '智能辅助诊断',
            '药物研发加速',
            '患者管理与随访',
            '医疗文档智能处理'
        ]
    },
    {
        name: '文旅传媒',
        icon: '🎬',
        scenarios: [
            'AIGC 内容创作',
            '智能推荐与分发',
            '视频智能处理',
            '数字人与虚拟主播',
            '用户增长与运营'
        ]
    },
    {
        name: '政企',
        icon: '🏛️',
        scenarios: [
            '政务智能客服',
            '城市大脑与智慧城市',
            '数据中台与共享',
            '智能办公与效率提升',
            '安全与应急管理'
        ]
    }
];

// ========== 初始化 ==========
document.addEventListener('DOMContentLoaded', () => {
    loadIdentity();
    loadData();
    renderIndustries();
    renderCustomerList();
    setupEventListeners();
});

// ========== 客户管理 ==========

// 从本地存储加载数据
function loadData() {
    try {
        const savedCustomers = localStorage.getItem('xiaoshouyi_customers');
        const savedRecords = localStorage.getItem('xiaoshouyi_records');
        if (savedCustomers) customers = JSON.parse(savedCustomers);
        if (savedRecords) records = JSON.parse(savedRecords);
    } catch (e) {
        console.error('加载数据失败:', e);
    }
}

// 保存数据到本地存储
function saveData() {
    try {
        localStorage.setItem('xiaoshouyi_customers', JSON.stringify(customers));
        localStorage.setItem('xiaoshouyi_records', JSON.stringify(records));
    } catch (e) {
        console.error('保存数据失败:', e);
    }
}

// 生成唯一ID
function generateId() {
    return Date.now().toString(36) + Math.random().toString(36).substr(2);
}

// 渲染客户列表
function renderCustomerList() {
    const grid = document.getElementById('customer-grid');
    const empty = document.getElementById('customer-empty');
    
    // 获取搜索和筛选条件
    const searchKeyword = document.getElementById('customer-search')?.value.trim().toLowerCase() || '';
    const stageFilter = document.getElementById('customer-stage-filter')?.value || '';
    
    // 过滤客户
    let filteredCustomers = customers.filter(customer => {
        // 阶段筛选
        if (stageFilter && customer.stage !== stageFilter) return false;
        
        // 关键词搜索
        if (searchKeyword) {
            const searchFields = [
                customer.name,
                customer.industry,
                customer.contact,
                customer.position,
                customer.notes,
                ...(customer.tags || [])
            ].filter(Boolean).map(s => s.toLowerCase());
            
            if (!searchFields.some(field => field.includes(searchKeyword))) return false;
        }
        
        return true;
    });
    
    if (filteredCustomers.length === 0) {
        grid.innerHTML = '';
        empty.classList.remove('hidden');
        if (searchKeyword || stageFilter) {
            empty.querySelector('h3').textContent = '没有找到匹配的客户';
            empty.querySelector('p').textContent = '试试换个关键词或筛选条件';
        } else {
            empty.querySelector('h3').textContent = '还没有客户';
            empty.querySelector('p').textContent = '点击右上角"新增客户"，开始管理你的客户资源';
        }
        return;
    }
    
    empty.classList.add('hidden');
    grid.innerHTML = filteredCustomers.map(customer => {
        const customerRecords = records.filter(r => r.customerId === customer.id);
        const avatar = customer.name.charAt(0);
        const stage = stageConfig.find(s => s.key === customer.stage) || stageConfig[0];
        return `
            <div class="bg-white rounded-2xl shadow-sm p-6 card-hover cursor-pointer" onclick="showCustomerDetail('${customer.id}')">
                <div class="flex items-start gap-4 mb-4">
                    <div class="w-12 h-12 rounded-xl bg-gradient-primary flex items-center justify-center text-white text-lg font-bold flex-shrink-0">
                        ${avatar}
                    </div>
                    <div class="flex-1 min-w-0">
                        <h3 class="font-bold text-dark truncate">${customer.name}</h3>
                        <p class="text-sm text-gray-500">${customer.industry || '未分类'}</p>
                    </div>
                </div>
                <div class="space-y-2 text-sm text-gray-600">
                    ${customer.contact ? `<div><i class="fa fa-user mr-2 text-gray-400"></i>${customer.contact}${customer.position ? ' · ' + customer.position : ''}</div>` : ''}
                    <div class="flex items-center justify-between">
                        <span class="inline-flex items-center gap-1">
                            <div class="w-2 h-2 rounded-full bg-${stage.color}-500"></div>
                            <span class="text-xs">${stage.label}</span>
                        </span>
                        <span class="text-xs font-medium text-primary">${customer.amount ? customer.amount + '万' : ''}</span>
                    </div>
                    ${customer.tags && customer.tags.length > 0 ? `
                        <div class="flex flex-wrap gap-1 mt-2">
                            ${customer.tags.slice(0, 3).map(tag => `<span class="px-2 py-0.5 bg-gray-100 text-gray-600 rounded text-xs">${tag}</span>`).join('')}
                            ${customer.tags.length > 3 ? `<span class="px-2 py-0.5 bg-gray-100 text-gray-600 rounded text-xs">+${customer.tags.length - 3}</span>` : ''}
                        </div>
                    ` : ''}
                </div>
                <div class="mt-4 pt-4 border-t border-gray-100 flex items-center justify-between">
                    <span class="text-xs text-gray-400">${customerRecords.length} 条记录</span>
                    <span class="text-primary text-sm font-medium">查看详情 <i class="fa fa-arrow-right ml-1"></i></span>
                </div>
            </div>
        `;
    }).join('');
}

// 显示新增客户弹窗
function showAddCustomerModal() {
    editingCustomerId = null;
    document.getElementById('modal-title').textContent = '新增客户';
    document.getElementById('modal-company-name').value = '';
    document.getElementById('modal-industry').value = '';
    document.getElementById('modal-contact').value = '';
    document.getElementById('modal-position').value = '';
    document.getElementById('modal-phone').value = '';
    document.getElementById('modal-email').value = '';
    document.getElementById('modal-notes').value = '';
    document.getElementById('modal-stage').value = 'lead';
    document.getElementById('modal-probability').value = 10;
    document.getElementById('modal-amount').value = '';
    document.getElementById('modal-next-followup').value = '';
    document.getElementById('modal-tags').value = '';
    document.getElementById('customer-modal').classList.remove('hidden');
}

// 显示编辑客户弹窗
function showEditCustomerModal(customerId) {
    const customer = customers.find(c => c.id === customerId);
    if (!customer) return;
    
    editingCustomerId = customerId;
    document.getElementById('modal-title').textContent = '编辑客户';
    document.getElementById('modal-company-name').value = customer.name || '';
    document.getElementById('modal-industry').value = customer.industry || '';
    document.getElementById('modal-contact').value = customer.contact || '';
    document.getElementById('modal-position').value = customer.position || '';
    document.getElementById('modal-phone').value = customer.phone || '';
    document.getElementById('modal-email').value = customer.email || '';
    document.getElementById('modal-notes').value = customer.notes || '';
    document.getElementById('modal-stage').value = customer.stage || 'lead';
    document.getElementById('modal-probability').value = customer.probability || 10;
    document.getElementById('modal-amount').value = customer.amount || '';
    document.getElementById('modal-next-followup').value = customer.nextFollowUp || '';
    document.getElementById('modal-tags').value = (customer.tags || []).join(', ');
    document.getElementById('customer-modal').classList.remove('hidden');
}

// 隐藏弹窗
function hideCustomerModal() {
    document.getElementById('customer-modal').classList.add('hidden');
    editingCustomerId = null;
}

// 保存客户
function saveCustomer() {
    const name = document.getElementById('modal-company-name').value.trim();
    if (!name) {
        alert('请输入公司名称');
        return;
    }
    
    const customerData = {
        name: name,
        industry: document.getElementById('modal-industry').value,
        contact: document.getElementById('modal-contact').value.trim(),
        position: document.getElementById('modal-position').value.trim(),
        phone: document.getElementById('modal-phone').value.trim(),
        email: document.getElementById('modal-email').value.trim(),
        notes: document.getElementById('modal-notes').value.trim(),
        stage: document.getElementById('modal-stage').value || 'lead',
        tags: document.getElementById('modal-tags').value.trim().split(',').map(t => t.trim()).filter(t => t),
        amount: parseFloat(document.getElementById('modal-amount').value) || 0,
        probability: parseInt(document.getElementById('modal-probability').value) || 10,
        nextFollowUp: document.getElementById('modal-next-followup').value || null,
    };
    
    if (editingCustomerId) {
        // 编辑
        const index = customers.findIndex(c => c.id === editingCustomerId);
        if (index !== -1) {
            customers[index] = { ...customers[index], ...customerData, updatedAt: new Date().toISOString() };
        }
    } else {
        // 新增
        const newCustomer = {
            id: generateId(),
            ...customerData,
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
        };
        customers.unshift(newCustomer);
    }
    
    saveData();
    renderCustomerList();
    hideCustomerModal();
    
    // 如果在详情页，刷新详情
    if (currentCustomerId === editingCustomerId) {
        renderCustomerDetail();
    }
}

// 编辑当前客户
function editCurrentCustomer() {
    if (currentCustomerId) {
        showEditCustomerModal(currentCustomerId);
    }
}

// 删除当前客户
function deleteCurrentCustomer() {
    if (!currentCustomerId) return;
    
    if (!confirm('确定要删除这个客户吗？所有历史记录也会被删除。')) return;
    
    // 删除客户
    customers = customers.filter(c => c.id !== currentCustomerId);
    // 删除相关记录
    records = records.filter(r => r.customerId !== currentCustomerId);
    
    saveData();
    showCustomerList();
}

// 显示客户详情
function showCustomerDetail(customerId) {
    currentCustomerId = customerId;
    document.getElementById('customer-list-view').classList.add('hidden');
    document.getElementById('customer-detail-view').classList.remove('hidden');
    renderCustomerDetail();
}

// 返回客户列表
function showCustomerList() {
    currentCustomerId = null;
    document.getElementById('customer-detail-view').classList.add('hidden');
    document.getElementById('customer-list-view').classList.remove('hidden');
    renderCustomerList();
}

// 渲染客户详情
function renderCustomerDetail() {
    const customer = customers.find(c => c.id === currentCustomerId);
    if (!customer) return;
    
    const stage = stageConfig.find(s => s.key === customer.stage) || stageConfig[0];
    
    document.getElementById('detail-avatar').textContent = customer.name.charAt(0);
    document.getElementById('detail-name').textContent = customer.name;
    document.getElementById('detail-industry').textContent = customer.industry || '未分类';
    document.getElementById('detail-contact').textContent = customer.contact || '暂无联系人';
    document.getElementById('detail-position').textContent = customer.position || '';
    document.getElementById('detail-notes').textContent = customer.notes || '';
    
    // 渲染客户信息头部的阶段和金额
    const infoHeader = document.querySelector('#customer-detail-view .bg-white.rounded-2xl');
    if (infoHeader && !document.getElementById('detail-stage-info')) {
        const stageInfo = document.createElement('div');
        stageInfo.id = 'detail-stage-info';
        stageInfo.className = 'mt-6 pt-6 border-t border-gray-100 grid grid-cols-2 md:grid-cols-4 gap-4';
        infoHeader.querySelector('.flex.items-start.justify-between').parentElement.appendChild(stageInfo);
    }
    
    const stageInfoEl = document.getElementById('detail-stage-info');
    if (stageInfoEl) {
        stageInfoEl.innerHTML = `
            <div>
                <div class="text-xs text-gray-500 mb-1">销售阶段</div>
                <div class="flex items-center gap-2">
                    <div class="w-2 h-2 rounded-full bg-${stage.color}-500"></div>
                    <span class="font-medium text-dark">${stage.label}</span>
                </div>
            </div>
            <div>
                <div class="text-xs text-gray-500 mb-1">预计金额</div>
                <div class="font-medium text-dark">${customer.amount ? customer.amount + ' 万' : '暂无'}</div>
            </div>
            <div>
                <div class="text-xs text-gray-500 mb-1">成交概率</div>
                <div class="font-medium text-${stage.color}-600">${customer.probability || stage.probability}%</div>
            </div>
            <div>
                <div class="text-xs text-gray-500 mb-1">下次跟进</div>
                <div class="font-medium ${customer.nextFollowUp && customer.nextFollowUp <= new Date().toISOString().split('T')[0] ? 'text-red-500' : 'text-dark'}">${customer.nextFollowUp || '暂无'}</div>
            </div>
        `;
    }
    
    // 渲染历史记录
    renderCustomerRecords();
}

// 渲染客户历史记录
function renderCustomerRecords() {
    const container = document.getElementById('customer-records');
    const empty = document.getElementById('records-empty');
    
    const customerRecords = records
        .filter(r => r.customerId === currentCustomerId)
        .sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt));
    
    if (customerRecords.length === 0) {
        container.innerHTML = '';
        empty.classList.remove('hidden');
        return;
    }
    
    empty.classList.add('hidden');
    
    const typeConfig = {
        research: { icon: 'fa-search', color: 'blue', label: '客户背调' },
        solution: { icon: 'fa-lightbulb-o', color: 'green', label: '方案建议书' },
        script: { icon: 'fa-microphone', color: 'purple', label: '销售话术' },
        objection: { icon: 'fa-shield', color: 'orange', label: '异议处理' },
        checklist: { icon: 'fa-check-square-o', color: 'teal', label: '拜访清单' },
        competitor: { icon: 'fa-balance-scale', color: 'indigo', label: '竞品对比' },
        followup: { icon: 'fa-phone', color: 'pink', label: '跟进记录' }
    };
    
    container.innerHTML = customerRecords.map(record => {
        const config = typeConfig[record.type] || { icon: 'fa-file', color: 'gray', label: '记录' };
        const date = new Date(record.createdAt).toLocaleString();
        return `
            <div class="bg-white rounded-xl shadow-sm p-5 card-hover">
                <div class="flex items-start justify-between">
                    <div class="flex items-start gap-4">
                        <div class="w-10 h-10 rounded-lg bg-${config.color}-100 flex items-center justify-center flex-shrink-0">
                            <i class="fa ${config.icon} text-${config.color}-600"></i>
                        </div>
                        <div>
                            <h4 class="font-semibold text-dark">${record.title}</h4>
                            <p class="text-sm text-gray-500 mt-1">${config.label} · ${date}</p>
                        </div>
                    </div>
                    <div class="flex gap-2">
                        <button onclick="viewRecord('${record.id}')" class="px-3 py-1 text-sm text-primary hover:bg-primary/5 rounded-lg transition-colors">
                            <i class="fa fa-eye mr-1"></i> 查看
                        </button>
                        <button onclick="deleteRecord('${record.id}')" class="px-3 py-1 text-sm text-red-500 hover:bg-red-50 rounded-lg transition-colors">
                            <i class="fa fa-trash mr-1"></i> 删除
                        </button>
                    </div>
                </div>
            </div>
        `;
    }).join('');
}

// 添加历史记录
function addRecord(customerId, type, title, content) {
    if (!customerId) return;
    
    const record = {
        id: generateId(),
        customerId: customerId,
        type: type,
        title: title,
        content: content,
        createdAt: new Date().toISOString()
    };
    
    records.unshift(record);
    saveData();
}

// 查看记录
function viewRecord(recordId) {
    const record = records.find(r => r.id === recordId);
    if (!record) return;
    
    // 这里可以做一个弹窗查看，或者跳转到对应页面
    // 简单起见，先复制到剪贴板并提示
    navigator.clipboard.writeText(record.content).then(() => {
        alert('内容已复制到剪贴板');
    });
}

// 删除记录
function deleteRecord(recordId) {
    if (!confirm('确定要删除这条记录吗？')) return;
    records = records.filter(r => r.id !== recordId);
    saveData();
    renderCustomerRecords();
}

// ========== 跟进记录 ==========

// 添加跟进记录
function addFollowUp(customerId, type, content, nextStep, nextFollowUp) {
    if (!customerId) return;
    
    const record = {
        id: generateId(),
        customerId: customerId,
        type: 'followup',
        followUpType: type,
        title: `${type}跟进`,
        content: content,
        nextStep: nextStep || '',
        nextFollowUp: nextFollowUp || null,
        createdAt: new Date().toISOString()
    };
    
    records.unshift(record);
    
    // 更新客户的下次跟进时间
    if (nextFollowUp) {
        const customer = customers.find(c => c.id === customerId);
        if (customer) {
            customer.nextFollowUp = nextFollowUp;
            customer.updatedAt = new Date().toISOString();
        }
    }
    
    saveData();
    return record;
}

// 显示添加跟进弹窗
function showAddFollowUpModal() {
    document.getElementById('followup-type').value = '电话';
    document.getElementById('followup-content').value = '';
    document.getElementById('followup-next-step').value = '';
    document.getElementById('followup-next-date').value = '';
    document.getElementById('followup-modal').classList.remove('hidden');
}

// 隐藏跟进弹窗
function hideFollowUpModal() {
    document.getElementById('followup-modal').classList.add('hidden');
}

// 保存跟进记录
function saveFollowUp() {
    const type = document.getElementById('followup-type').value;
    const content = document.getElementById('followup-content').value.trim();
    const nextStep = document.getElementById('followup-next-step').value.trim();
    const nextFollowUp = document.getElementById('followup-next-date').value;
    
    if (!content) {
        alert('请填写跟进内容');
        return;
    }
    
    addFollowUp(currentCustomerId, type, content, nextStep, nextFollowUp);
    hideFollowUpModal();
    renderCustomerDetail();
    renderCustomerRecords();
}

// ========== 销售看板 ==========

const stageConfig = [
    { key: 'lead', label: '潜在客户', color: 'gray', probability: 10, icon: 'fa-user-o' },
    { key: 'contact', label: '初步接触', color: 'blue', probability: 20, icon: 'fa-phone' },
    { key: 'requirement', label: '需求确认', color: 'cyan', probability: 40, icon: 'fa-comments' },
    { key: 'proposal', label: '方案沟通', color: 'purple', probability: 60, icon: 'fa-file-text-o' },
    { key: 'negotiation', label: '商务谈判', color: 'orange', probability: 80, icon: 'fa-handshake-o' },
    { key: 'won', label: '签约成交', color: 'green', probability: 100, icon: 'fa-trophy' },
    { key: 'lost', label: '流失', color: 'red', probability: 0, icon: 'fa-times' }
];

// 渲染销售看板
function renderPipeline() {
    const activeCustomers = customers.filter(c => c.stage !== 'lost');
    const totalAmount = activeCustomers.reduce((sum, c) => sum + (c.amount || 0), 0);
    const weightedAmount = activeCustomers.reduce((sum, c) => sum + (c.amount || 0) * (c.probability || 0) / 100, 0);
    
    // 计算待跟进数量（今天及之前的）
    const today = new Date().toISOString().split('T')[0];
    const followupCount = customers.filter(c => c.nextFollowUp && c.nextFollowUp <= today && c.stage !== 'lost').length;
    
    // 更新统计卡片
    document.getElementById('stat-total-customers').textContent = activeCustomers.length;
    document.getElementById('stat-total-amount').textContent = totalAmount.toFixed(1);
    document.getElementById('stat-weighted-amount').textContent = weightedAmount.toFixed(1);
    document.getElementById('stat-followup').textContent = followupCount;
    
    // 渲染漏斗
    renderPipelineFunnel();
    
    // 渲染各阶段客户
    renderPipelineStages();
}

// 渲染销售漏斗
function renderPipelineFunnel() {
    const container = document.getElementById('pipeline-funnel');
    const maxCount = Math.max(...stageConfig.map(s => customers.filter(c => c.stage === s.key).length), 1);
    
    container.innerHTML = stageConfig.map(stage => {
        const stageCustomers = customers.filter(c => c.stage === stage.key);
        const count = stageCustomers.length;
        const amount = stageCustomers.reduce((sum, c) => sum + (c.amount || 0), 0);
        const widthPercent = Math.max((count / maxCount) * 100, 15);
        
        return `
            <div class="flex items-center gap-4">
                <div class="w-28 text-sm font-medium text-gray-600 flex-shrink-0">${stage.label}</div>
                <div class="flex-1 h-12 bg-${stage.color}-100 rounded-lg relative overflow-hidden" style="width: ${widthPercent}%">
                    <div class="absolute inset-0 flex items-center justify-between px-4">
                        <span class="text-sm font-semibold text-${stage.color}-700">${count} 个</span>
                        <span class="text-sm text-${stage.color}-600">${amount.toFixed(1)}万</span>
                    </div>
                </div>
                <div class="w-16 text-sm text-gray-500 text-right flex-shrink-0">${stage.probability}%</div>
            </div>
        `;
    }).join('');
}

// 渲染各阶段客户列表
function renderPipelineStages() {
    const container = document.getElementById('pipeline-stages');
    
    container.innerHTML = stageConfig.map(stage => {
        const stageCustomers = customers.filter(c => c.stage === stage.key);
        if (stageCustomers.length === 0) return '';
        
        return `
            <div>
                <div class="flex items-center gap-2 mb-3">
                    <div class="w-3 h-3 rounded-full bg-${stage.color}-500"></div>
                    <h4 class="font-semibold text-dark">${stage.label}</h4>
                    <span class="text-sm text-gray-500">(${stageCustomers.length}个)</span>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
                    ${stageCustomers.map(c => `
                        <div class="border border-gray-100 rounded-xl p-4 hover:border-primary/30 hover:bg-primary/5 transition-all cursor-pointer" onclick="showCustomerDetail('${c.id}')">
                            <div class="font-medium text-dark mb-1">${c.name}</div>
                            <div class="text-sm text-gray-500 mb-2">${c.industry || '未分类'} · ${c.contact || '暂无联系人'}</div>
                            <div class="flex items-center justify-between text-sm">
                                <span class="text-gray-600">${c.amount ? c.amount + '万' : '暂无金额'}</span>
                                <span class="text-${stage.color}-600 font-medium">${stage.probability}%</span>
                            </div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }).join('');
}

// ========== 快捷功能联动 ==========

// 从客户详情生成背调
function generateResearchFromCustomer() {
    const customer = customers.find(c => c.id === currentCustomerId);
    if (!customer) return;
    
    // 跳转到背调页面，自动填充
    showSection('research');
    document.getElementById('company-name').value = customer.name;
    document.getElementById('research-industry').value = customer.industry || '';
    document.getElementById('research-position').value = customer.position || '';
}

// 从客户详情生成方案
function generateSolutionFromCustomer() {
    const customer = customers.find(c => c.id === currentCustomerId);
    if (!customer) return;
    
    // 跳转到方案页面，自动填充行业
    showSection('solution');
    if (customer.industry) {
        // 找到对应的行业索引并选中
        const industryIndex = industries.findIndex(i => i.name === customer.industry);
        if (industryIndex !== -1) {
            selectIndustry(industryIndex);
        }
    }
}

// 从客户详情生成话术
function generateScriptFromCustomer() {
    const customer = customers.find(c => c.id === currentCustomerId);
    if (!customer) return;
    
    showSection('tools');
    // 可以自动填充，这里先简单跳转
    alert('已跳转到销售工具箱，请填写相关信息');
}

// 从客户详情生成异议处理
function generateObjectionFromCustomer() {
    showSection('tools');
    alert('已跳转到销售工具箱，请填写异议内容');
}

// 从客户详情生成拜访清单
function generateChecklistFromCustomer() {
    const customer = customers.find(c => c.id === currentCustomerId);
    if (!customer) return;
    
    showSection('tools');
    document.getElementById('visit-company').value = customer.name;
    document.getElementById('visit-industry').value = customer.industry || '';
    document.getElementById('visit-position').value = customer.position || '';
}

// 从客户详情打开ROI
function showROIFromCustomer() {
    showSection('tools');
    // 滚动到ROI计算器
    setTimeout(() => {
        document.getElementById('roi-calculator')?.scrollIntoView({ behavior: 'smooth' });
    }, 100);
}

// ========== 页面切换 ==========
// ========== 身份选择 ==========
let identityIndustry = "";
let identitySalesType = "";

function showIdentityModal() {
    document.getElementById('identity-modal').classList.remove('hidden');
    // 重置选中状态
    identityIndustry = "";
    identitySalesType = "";
    updateIdentitySelectionUI();
}

function hideIdentityModal() {
    document.getElementById('identity-modal').classList.add('hidden');
}

function selectIdentityIndustry(industry) {
    identityIndustry = industry;
    updateIdentitySelectionUI();
}

function selectSalesType(salesType) {
    identitySalesType = salesType;
    updateIdentitySelectionUI();
}

function updateIdentitySelectionUI() {
    // 更新行业选中状态
    document.querySelectorAll('.industry-option').forEach(btn => {
        btn.classList.remove('border-gray-900', 'bg-gray-50');
        btn.classList.add('border-gray-200');
    });
    if (identityIndustry) {
        document.querySelectorAll('.industry-option').forEach(btn => {
            if (btn.textContent.includes(identityIndustry)) {
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
    if (identitySalesType) {
        document.querySelectorAll('.sales-type-option').forEach(btn => {
            if (btn.textContent.includes(identitySalesType)) {
                btn.classList.remove('border-gray-200');
                btn.classList.add('border-gray-900', 'bg-gray-50');
            }
        });
    }
    
    // 更新确认按钮状态
    const confirmBtn = document.getElementById('confirm-identity-btn');
    if (confirmBtn) {
        if (identityIndustry && identitySalesType) {
            confirmBtn.disabled = false;
            confirmBtn.classList.remove('bg-gray-300', 'cursor-not-allowed');
            confirmBtn.classList.add('bg-gray-900', 'hover:bg-gray-800', 'cursor-pointer');
            confirmBtn.textContent = `确认：${identityIndustry} · ${identitySalesType}`;
        } else {
            confirmBtn.disabled = true;
            confirmBtn.classList.add('bg-gray-300', 'cursor-not-allowed');
            confirmBtn.classList.remove('bg-gray-900', 'hover:bg-gray-800', 'cursor-pointer');
            if (!identityIndustry) {
                confirmBtn.textContent = "请先选择行业";
            } else {
                confirmBtn.textContent = "请选择销售类型";
            }
        }
    }
}

function confirmIdentity() {
    if (!identityIndustry || !identitySalesType) return;
    
    const identity = `${identityIndustry} · ${identitySalesType}`;
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


// ========== 文件上传 ==========
function toggleUploadMenu() {
    const menu = document.getElementById('upload-menu');
    if (menu) {
        menu.classList.toggle('hidden');
    }
}

// 点击页面其他地方关闭上传菜单
document.addEventListener('click', function(e) {
    const menu = document.getElementById('upload-menu');
    const plusBtn = e.target.closest('button');
    if (menu && !menu.contains(e.target) && !e.target.closest('[onclick*="toggleUploadMenu"]')) {
        menu.classList.add('hidden');
    }
});

function uploadBidDocument() {
    const menu = document.getElementById('upload-menu');
    if (menu) menu.classList.add('hidden');
    
    const fileInput = document.getElementById('bid-file-input');
    if (fileInput) {
        fileInput.click();
    }
}

// 文件选择后处理
document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('bid-file-input');
    if (fileInput) {
        fileInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                handleBidFileUpload(file);
            }
        });
    }
});

function handleBidFileUpload(file) {
    // 检查文件大小（限制10MB）
    if (file.size > 10 * 1024 * 1024) {
        alert('文件大小不能超过10MB');
        return;
    }
    
    // 检查文件类型
    const allowedTypes = ['application/pdf', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'text/plain'];
    if (!allowedTypes.includes(file.type) && !file.name.endsWith('.pdf') && !file.name.endsWith('.doc') && !file.name.endsWith('.docx') && !file.name.endsWith('.txt')) {
        alert('仅支持 PDF、Word、TXT 格式');
        return;
    }
    
    // 跳转到结果页面并显示加载状态
    showSection('bid-analysis');
    showBidAnalysisLoading(file.name);
    
    // 上传文件
    const formData = new FormData();
    formData.append('file', file);
    formData.append('identity', currentIdentity);
    
    fetch(`${API_BASE_URL}/bid/analyze`, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            renderBidAnalysisResult(data.data);
        } else {
            showBidAnalysisError(data.message || '分析失败，请稍后重试');
        }
    })
    .catch(error => {
        console.error('上传失败:', error);
        showBidAnalysisError('上传失败，请检查网络连接');
    });
}

function showBidAnalysisLoading(filename) {
    const container = document.getElementById('bid-analysis-content');
    if (container) {
        container.innerHTML = `
            <div class="flex flex-col items-center justify-center py-20">
                <div class="w-12 h-12 border-4 border-gray-200 border-t-gray-900 rounded-full animate-spin mb-4"></div>
                <div class="text-gray-600 font-medium mb-2">正在分析招标文件</div>
                <div class="text-gray-400 text-sm">${filename}</div>
                <div class="text-gray-400 text-sm mt-4">AI 正在提炼关键需求和风险点，请稍候...</div>
            </div>
        `;
    }
}

function showBidAnalysisError(message) {
    const container = document.getElementById('bid-analysis-content');
    if (container) {
        container.innerHTML = `
            <div class="flex flex-col items-center justify-center py-20">
                <div class="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center mb-4">
                    <i class="fa fa-exclamation-triangle text-red-500 text-2xl"></i>
                </div>
                <div class="text-gray-700 font-medium mb-2">分析失败</div>
                <div class="text-gray-500 text-sm mb-6">${message}</div>
                <button onclick="showSection('hero')" class="px-6 py-2.5 bg-gray-900 text-white rounded-xl hover:bg-gray-800 transition-all">
                    返回首页
                </button>
            </div>
        `;
    }
}

function renderBidAnalysisResult(data) {
    const container = document.getElementById('bid-analysis-content');
    if (!container) return;
    
    let html = `
        <!-- 项目基本信息 -->
        <div class="bg-gray-50 rounded-2xl p-6 mb-6">
            <h3 class="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                <i class="fa fa-info-circle text-gray-500"></i>
                项目基本信息
            </h3>
            <div class="grid grid-cols-2 gap-4">
                <div>
                    <div class="text-sm text-gray-500 mb-1">项目名称</div>
                    <div class="font-medium text-gray-900">${data.project_name || '待确认'}</div>
                </div>
                <div>
                    <div class="text-sm text-gray-500 mb-1">采购方</div>
                    <div class="font-medium text-gray-900">${data.buyer || '待确认'}</div>
                </div>
                <div>
                    <div class="text-sm text-gray-500 mb-1">预算金额</div>
                    <div class="font-medium text-gray-900">${data.budget || '待确认'}</div>
                </div>
                <div>
                    <div class="text-sm text-gray-500 mb-1">交付周期</div>
                    <div class="font-medium text-gray-900">${data.duration || '待确认'}</div>
                </div>
                <div>
                    <div class="text-sm text-gray-500 mb-1">投标截止时间</div>
                    <div class="font-medium text-red-600">${data.deadline || '待确认'}</div>
                </div>
                <div>
                    <div class="text-sm text-gray-500 mb-1">项目地点</div>
                    <div class="font-medium text-gray-900">${data.location || '待确认'}</div>
                </div>
            </div>
        </div>
        
        <!-- 关键需求 -->
        <div class="bg-white border border-gray-200 rounded-2xl p-6 mb-6">
            <h3 class="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                <i class="fa fa-list-check text-blue-500"></i>
                关键需求清单
            </h3>
    `;
    
    // 技术需求
    if (data.technical_requirements && data.technical_requirements.length > 0) {
        html += `
            <div class="mb-5">
                <h4 class="font-semibold text-gray-800 mb-3 text-sm">技术需求</h4>
                <ul class="space-y-2">
        `;
        data.technical_requirements.forEach(req => {
            html += `
                    <li class="flex items-start gap-2 text-sm text-gray-600">
                        <i class="fa fa-check-circle text-blue-500 mt-0.5 flex-shrink-0"></i>
                        <span>${req}</span>
                    </li>
            `;
        });
        html += `
                </ul>
            </div>
        `;
    }
    
    // 服务需求
    if (data.service_requirements && data.service_requirements.length > 0) {
        html += `
            <div class="mb-5">
                <h4 class="font-semibold text-gray-800 mb-3 text-sm">服务需求</h4>
                <ul class="space-y-2">
        `;
        data.service_requirements.forEach(req => {
            html += `
                    <li class="flex items-start gap-2 text-sm text-gray-600">
                        <i class="fa fa-check-circle text-green-500 mt-0.5 flex-shrink-0"></i>
                        <span>${req}</span>
                    </li>
            `;
        });
        html += `
                </ul>
            </div>
        `;
    }
    
    // 商务需求
    if (data.business_requirements && data.business_requirements.length > 0) {
        html += `
            <div>
                <h4 class="font-semibold text-gray-800 mb-3 text-sm">商务要求</h4>
                <ul class="space-y-2">
        `;
        data.business_requirements.forEach(req => {
            html += `
                    <li class="flex items-start gap-2 text-sm text-gray-600">
                        <i class="fa fa-check-circle text-purple-500 mt-0.5 flex-shrink-0"></i>
                        <span>${req}</span>
                    </li>
            `;
        });
        html += `
                </ul>
            </div>
        `;
    }
    
    html += `
        </div>
        
        <!-- 风险点提示 -->
        <div class="bg-white border border-red-200 rounded-2xl p-6 mb-6">
            <h3 class="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                <i class="fa fa-exclamation-triangle text-red-500"></i>
                风险点提示
            </h3>
            <div class="space-y-3">
    `;
    
    if (data.risks && data.risks.length > 0) {
        data.risks.forEach((risk, index) => {
            html += `
                <div class="bg-red-50 rounded-xl p-4">
                    <div class="flex items-start gap-3">
                        <span class="w-6 h-6 bg-red-500 text-white rounded-full flex items-center justify-center text-xs font-bold flex-shrink-0">${index + 1}</span>
                        <div class="flex-1">
                            <div class="font-medium text-gray-900 text-sm mb-1">${risk.title || '风险点'}</div>
                            <div class="text-gray-600 text-sm">${risk.description || ''}</div>
                            ${risk.suggestion ? `<div class="mt-2 text-sm text-green-700"><i class="fa fa-lightbulb-o mr-1"></i>建议：${risk.suggestion}</div>` : ''}
                        </div>
                    </div>
                </div>
            `;
        });
    } else {
        html += `
                <div class="text-gray-500 text-sm">未发现明显风险点</div>
        `;
    }
    
    html += `
            </div>
        </div>
        
        <!-- 应对建议 -->
        <div class="bg-white border border-gray-200 rounded-2xl p-6">
            <h3 class="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                <i class="fa fa-lightbulb-o text-yellow-500"></i>
                应对建议
            </h3>
            <ol class="space-y-3 list-decimal list-inside">
    `;
    
    if (data.suggestions && data.suggestions.length > 0) {
        data.suggestions.forEach(suggestion => {
            html += `
                <li class="text-gray-600 text-sm">${suggestion}</li>
            `;
        });
    } else {
        html += `
                <li class="text-gray-500 text-sm">暂无建议</li>
        `;
    }
    
    html += `
            </ol>
        </div>
    `;
    
    container.innerHTML = html;
}

// ========== 页面切换 ==========
function showSection(sectionId) {
    // 隐藏所有 section
    document.querySelectorAll('.section').forEach(s => s.classList.add('hidden'));
    // 显示目标 section
    document.getElementById(sectionId).classList.remove('hidden');
    // 滚动到顶部
    window.scrollTo({ top: 0, behavior: 'smooth' });
    
    // 更新侧边栏选中状态
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('bg-gray-200', 'font-semibold');
        const icon = item.querySelector('i');
        if (icon) icon.classList.remove('text-gray-900');
    });
    const activeNav = document.querySelector(`.nav-item[data-section="${sectionId}"]`);
    if (activeNav) {
        activeNav.classList.add('bg-gray-200', 'font-semibold');
        const icon = activeNav.querySelector('i');
        if (icon) icon.classList.add('text-gray-900');
    }
    
    // 如果是销售看板，重新渲染
    if (sectionId === 'pipeline') {
        renderPipeline();
    }
}

// 首页对话功能
function heroChat() {
    const input = document.getElementById('hero-chat-input');
    const message = input.value.trim();
    if (!message) return;
    
    // 跳转到聊天页面，并自动发送消息
    showSection('chat');
    setTimeout(() => {
        // 找到聊天输入框，填入消息并发送
        const chatInput = document.getElementById('chat-input');
        if (chatInput) {
            chatInput.value = message;
            sendMessage();
        }
    }, 300);
}

// 滚动到产品介绍区
function scrollToIntro() {
    // 找到产品介绍区（hero 后面的第一个 section）
    const hero = document.getElementById('hero');
    const introSection = hero.nextElementSibling;
    if (introSection) {
        introSection.scrollIntoView({ behavior: 'smooth' });
    }
}

// ========== 行业选择 ==========
function renderIndustries() {
    const grid = document.getElementById('industry-grid');
    grid.innerHTML = industries.map(ind => `
        <div onclick="selectIndustry('${ind.name}')" 
             class="industry-card p-4 border border-gray-200 rounded-xl cursor-pointer transition-all hover:border-primary hover:bg-primary/5 text-center"
             data-industry="${ind.name}">
            <div class="text-2xl mb-2">${ind.icon}</div>
            <div class="text-sm font-medium text-gray-700">${ind.name}</div>
        </div>
    `).join('');
}

function selectIndustry(industryName) {
    selectedIndustry = industryName;
    selectedScenario = null;
    
    // 更新选中状态
    document.querySelectorAll('.industry-card').forEach(card => {
        if (card.dataset.industry === industryName) {
            card.classList.add('border-primary', 'bg-primary/5', 'ring-2', 'ring-primary/20');
        } else {
            card.classList.remove('border-primary', 'bg-primary/5', 'ring-2', 'ring-primary/20');
        }
    });
    
    // 更新步骤指示器
    document.getElementById('step1-dot').className = 'w-8 h-8 rounded-full bg-primary text-white flex items-center justify-center text-sm font-bold';
    document.getElementById('step2-dot').className = 'w-8 h-8 rounded-full bg-primary text-white flex items-center justify-center text-sm font-bold';
    
    // 显示场景选择
    renderScenarios(industryName);
    document.getElementById('scenario-card').classList.remove('hidden');
    document.getElementById('advanced-card').classList.add('hidden');
    document.getElementById('generate-btn').classList.add('hidden');
}

function renderScenarios(industryName) {
    const industry = industries.find(i => i.name === industryName);
    if (!industry) return;
    
    const list = document.getElementById('scenario-list');
    list.innerHTML = industry.scenarios.map(scenario => `
        <div onclick="selectScenario('${scenario}')" 
             class="scenario-item p-3 border border-gray-200 rounded-lg cursor-pointer transition-all hover:border-primary hover:bg-primary/5 text-sm"
             data-scenario="${scenario}">
            <i class="fa fa-circle-o text-gray-400 mr-2 text-xs"></i>
            ${scenario}
        </div>
    `).join('');
}

function selectScenario(scenario) {
    selectedScenario = scenario;
    
    // 更新选中状态
    document.querySelectorAll('.scenario-item').forEach(item => {
        if (item.dataset.scenario === scenario) {
            item.classList.add('border-primary', 'bg-primary/5', 'ring-2', 'ring-primary/20');
            item.querySelector('i').className = 'fa fa-check-circle text-primary mr-2 text-xs';
        } else {
            item.classList.remove('border-primary', 'bg-primary/5', 'ring-2', 'ring-primary/20');
            item.querySelector('i').className = 'fa fa-circle-o text-gray-400 mr-2 text-xs';
        }
    });
    
    // 更新步骤指示器
    document.getElementById('step3-dot').className = 'w-8 h-8 rounded-full bg-primary text-white flex items-center justify-center text-sm font-bold';
    
    // 显示高级选项和生成按钮
    document.getElementById('advanced-card').classList.remove('hidden');
    document.getElementById('generate-btn').classList.remove('hidden');
}

// ========== 方案生成 ==========
async function generateSolution() {
    if (!selectedIndustry || !selectedScenario) {
        alert('请先选择行业和场景');
        return;
    }
    
    const btn = document.getElementById('generate-btn');
    const emptyState = document.getElementById('empty-state');
    const loadingState = document.getElementById('loading-state');
    const solutionMarkdown = document.getElementById('solution-markdown');
    const solutionHeader = document.getElementById('solution-header');
    const adjustBar = document.getElementById('adjust-bar');
    
    // 显示加载状态
    btn.disabled = true;
    btn.innerHTML = '<i class="fa fa-spinner fa-spin mr-2"></i> 生成中...';
    emptyState.classList.add('hidden');
    solutionMarkdown.classList.add('hidden');
    solutionHeader.classList.add('hidden');
    adjustBar.classList.add('hidden');
    loadingState.classList.remove('hidden');
    
    // 模拟加载进度文字
    const loadingTexts = [
        '正在分析行业痛点...',
        '正在匹配产品方案...',
        '正在生成方案架构...',
        '正在计算 ROI 估算...',
        '正在完善方案细节...'
    ];
    let textIndex = 0;
    const loadingInterval = setInterval(() => {
        textIndex = (textIndex + 1) % loadingTexts.length;
        document.getElementById('loading-text').textContent = loadingTexts[textIndex];
    }, 1500);
    
    try {
        const companySize = document.getElementById('company-size').value;
        const customReq = document.getElementById('custom-req').value;
        
        // 调用流式接口
        const response = await fetch(`${API_BASE_URL}/solution/generate-stream`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                industry: selectedIndustry,
                scenario: selectedScenario,
                company_size: companySize,
                custom_requirements: customReq,
                identity: currentIdentity
            })
        });
        
        if (!response.ok) {
            throw new Error('生成失败');
        }
        
        // 切换到显示内容状态
        clearInterval(loadingInterval);
        loadingState.classList.add('hidden');
        solutionHeader.classList.remove('hidden');
        solutionMarkdown.classList.remove('hidden');
        adjustBar.classList.remove('hidden');
        
        // 读取 SSE 流
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let fullContent = '';
        
        while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            
            const chunk = decoder.decode(value);
            const lines = chunk.split('\n');
            
            for (const line of lines) {
                if (line.startsWith('data: ')) {
                    const data = line.slice(6);
                    if (data === '[DONE]') {
                        // 生成完成
                        break;
                    }
                    try {
                        const parsed = JSON.parse(data);
                        if (parsed.content) {
                            fullContent += parsed.content;
                            // 实时渲染 Markdown
                            solutionMarkdown.innerHTML = marked.parse(fullContent);
                            // 滚动到底部
                            solutionMarkdown.scrollTop = solutionMarkdown.scrollHeight;
                        }
                    } catch (e) {
                        // 忽略解析错误
                    }
                }
            }
        }
        
        // 保存当前方案
        currentSolution = {
            industry: selectedIndustry,
            scenario: selectedScenario,
            content: fullContent,
            products: extractProductsFromContent(fullContent)
        };
        
        // 如果有当前客户，保存到历史记录
        if (currentCustomerId) {
            addRecord(currentCustomerId, 'solution', 
                `${selectedIndustry}行业${selectedScenario}解决方案`, 
                fullContent);
        }
        
        // 渲染产品标签
        renderProductTags(currentSolution.products);
        
    } catch (error) {
        console.error('生成方案失败:', error);
        alert('生成方案失败，请检查后端服务是否启动');
        emptyState.classList.remove('hidden');
    } finally {
        clearInterval(loadingInterval);
        loadingState.classList.add('hidden');
        btn.disabled = false;
        btn.innerHTML = '<i class="fa fa-magic mr-2"></i> 生成方案建议书';
    }
}

// 从内容中提取产品（简单版，流式生成时用）
function extractProductsFromContent(content) {
    const products = [];
    const productNames = [
        '豆包大模型', '火山方舟', '智能推荐引擎', '智能客服',
        '数据中台', '视觉智能', '语音技术', '视频云', '内容安全'
    ];
    for (const name of productNames) {
        if (content.includes(name)) {
            products.push(name);
        }
    }
    return products;
}

function renderSolution(data) {
    const solutionHeader = document.getElementById('solution-header');
    const solutionMarkdown = document.getElementById('solution-markdown');
    const adjustBar = document.getElementById('adjust-bar');
    
    // 更新标题
    document.getElementById('solution-title').textContent = `${data.industry}行业解决方案建议书`;
    document.getElementById('solution-subtitle').textContent = `场景：${data.scenario} · 企业规模：${data.company_size}`;
    
    // 产品标签
    renderProductTags(data.products);
    
    // 渲染 Markdown
    solutionMarkdown.innerHTML = marked.parse(data.content);
    
    // 显示
    solutionHeader.classList.remove('hidden');
    solutionMarkdown.classList.remove('hidden');
    adjustBar.classList.remove('hidden');
}

function renderProductTags(products) {
    const productTags = document.getElementById('product-tags');
    if (!productTags || !products) return;
    productTags.innerHTML = products.map(p => `
        <span class="px-3 py-1 bg-primary/10 text-primary text-xs rounded-full">${p}</span>
    `).join('');
}

async function adjustSolution() {
    const adjustment = document.getElementById('adjust-input').value.trim();
    if (!adjustment) {
        alert('请输入调整需求');
        return;
    }
    
    if (!currentSolution) {
        alert('请先生成方案');
        return;
    }
    
    const btn = event.target;
    btn.disabled = true;
    btn.innerHTML = '<i class="fa fa-spinner fa-spin mr-1"></i> 调整中...';
    
    try {
        const response = await fetch(`${API_BASE_URL}/solution/adjust`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                original_content: currentSolution.content,
                adjustment: adjustment
            })
        });
        
        if (!response.ok) {
            throw new Error('调整失败');
        }
        
        const data = await response.json();
        currentSolution.content = data.content;
        
        // 重新渲染
        document.getElementById('solution-markdown').innerHTML = marked.parse(data.content);
        document.getElementById('adjust-input').value = '';
        
        // 滚动到顶部
        document.getElementById('solution-content').scrollTop = 0;
        
    } catch (error) {
        console.error('调整方案失败:', error);
        alert('调整方案失败');
    } finally {
        btn.disabled = false;
        btn.innerHTML = '<i class="fa fa-refresh mr-1"></i> 调整方案';
    }
}

function copySolution() {
    if (!currentSolution) return;
    
    navigator.clipboard.writeText(currentSolution.content).then(() => {
        alert('方案已复制到剪贴板');
    });
}

function downloadSolution() {
    if (!currentSolution) return;
    
    const blob = new Blob([currentSolution.content], { type: 'text/markdown' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${currentSolution.industry}_${currentSolution.scenario}_解决方案.md`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

// ========== 智能对话 ==========
function quickChat(text) {
    const input = document.getElementById('chat-input');
    input.value = text;
    sendMessage();
}

async function sendMessage() {
    const input = document.getElementById('chat-input');
    const message = input.value.trim();
    
    if (!message) return;
    
    // 添加用户消息
    addChatMessage('user', message);
    input.value = '';
    
    // 添加 AI 空消息，用于流式填充
    const messageId = addChatMessage('assistant', '', false);
    const messageEl = document.getElementById(`chat-msg-${messageId}`);
    const contentEl = messageEl.querySelector('.chat-content');
    
    try {
        const response = await fetch(`${API_BASE_URL}/chat/stream`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                message: message,
                history: chatHistory,
                identity: currentIdentity
            })
        });
        
        if (!response.ok) {
            throw new Error('对话失败');
        }
        
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let fullReply = '';
        
        while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            
            const chunk = decoder.decode(value);
            const lines = chunk.split('\n\n');
            
            for (const line of lines) {
                if (line.startsWith('data: ')) {
                    const content = line.slice(6);
                    if (content) {
                        fullReply += content;
                        contentEl.textContent = fullReply;
                        // 自动滚动到底部
                        const chatMessages = document.getElementById('chat-messages');
                        chatMessages.scrollTop = chatMessages.scrollHeight;
                    }
                }
            }
        }
        
        // 流式输出完成后，渲染 Markdown
        contentEl.innerHTML = marked.parse(fullReply);
        
        // 保存到历史记录
        chatHistory.push({ role: 'user', content: message });
        chatHistory.push({ role: 'assistant', content: fullReply });
        
        // 自动滚动到底部
        const chatMessages = document.getElementById('chat-messages');
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
    } catch (error) {
        console.error('对话失败:', error);
        contentEl.textContent = '抱歉，出了点问题，请稍后再试。';
    }
}
function addChatMessage(role, content, isThinking = false) {
    const messagesContainer = document.getElementById('chat-messages');
    const id = 'chat-msg-' + Date.now();
    
    const messageHtml = role === 'user' 
        ? `
            <div id="${id}" class="flex items-start space-x-3 justify-end">
                <div class="bg-gray-900 text-white rounded-2xl rounded-tr-none px-4 py-3 max-w-[80%]">
                    <p>${escapeHtml(content)}</p>
                </div>
                <div class="w-8 h-8 rounded-full bg-gray-200 flex items-center justify-center flex-shrink-0">
                    <i class="fa fa-user text-gray-500 text-sm"></i>
                </div>
            </div>
        `
        : `
            <div id="${id}" class="flex items-start space-x-3">
                <div class="w-8 h-8 rounded-full bg-gray-900 flex items-center justify-center flex-shrink-0">
                    <span class="text-white text-sm font-bold italic">S</span>
                </div>
                <div class="bg-gray-100 rounded-2xl rounded-tl-none px-4 py-3 max-w-[80%]">
                    <div class="chat-content text-gray-800 prose prose-sm max-w-none ${isThinking ? 'typing-cursor' : ''}">
                        ${isThinking ? content : ''}
                    </div>
                </div>
            </div>
        `;
    
    messagesContainer.insertAdjacentHTML('beforeend', messageHtml);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
    
    return id;
}

function removeChatMessage(id) {
    const msg = document.getElementById(id);
    if (msg) msg.remove();
}

// ========== 销售工具箱 ==========
async function generateSalesScript() {
    const industry = document.getElementById('script-industry').value;
    const scenario = document.getElementById('script-scenario').value.trim();
    
    if (!scenario) {
        alert('请输入业务场景');
        return;
    }
    
    const btn = event.target;
    btn.disabled = true;
    btn.innerHTML = '<i class="fa fa-spinner fa-spin mr-1"></i> 生成中...';
    
    try {
        const response = await fetch(`${API_BASE_URL}/sales-script`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                industry: industry,
                scenario: scenario,
                identity: currentIdentity,
            })
        });
        
        if (!response.ok) {
            throw new Error('生成失败');
        }
        
        const data = await response.json();
        
        document.getElementById('script-content').innerHTML = marked.parse(data.script);
        document.getElementById('script-result').classList.remove('hidden');
        
        // 如果有当前客户，保存到历史记录
        if (currentCustomerId) {
            const industry = document.getElementById('script-industry').value;
            const scenario = document.getElementById('script-scenario').value;
            addRecord(currentCustomerId, 'script', 
                `${industry || ''}${scenario || ''}销售话术`, 
                data.script);
        }
        
    } catch (error) {
        console.error('生成话术失败:', error);
        alert('生成失败，请检查后端服务');
    } finally {
        btn.disabled = false;
        btn.innerHTML = '<i class="fa fa-magic mr-1"></i> 生成话术';
    }
}

function setObjection(text) {
    document.getElementById('objection-input').value = text;
}

async function handleObjection() {
    const objection = document.getElementById('objection-input').value.trim();
    const industry = document.getElementById('objection-industry').value.trim();
    
    if (!objection) {
        alert('请输入客户异议');
        return;
    }
    
    const btn = event.target;
    btn.disabled = true;
    btn.innerHTML = '<i class="fa fa-spinner fa-spin mr-1"></i> 生成中...';
    
    try {
        const response = await fetch(`${API_BASE_URL}/objection`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                objection: objection,
                industry: industry,
                identity: currentIdentity,
            })
        });
        
        if (!response.ok) {
            throw new Error('生成失败');
        }
        
        const data = await response.json();
        
        document.getElementById('objection-content').innerHTML = marked.parse(data.response);
        document.getElementById('objection-result').classList.remove('hidden');
        
        // 如果有当前客户，保存到历史记录
        if (currentCustomerId) {
            const objection = document.getElementById('objection-input').value.trim();
            addRecord(currentCustomerId, 'objection', 
                `异议处理：${objection.substring(0, 20)}...`, 
                data.response);
        }
        
    } catch (error) {
        console.error('生成应对话术失败:', error);
        alert('生成失败，请检查后端服务');
    } finally {
        btn.disabled = false;
        btn.innerHTML = '<i class="fa fa-lightbulb-o mr-1"></i> 生成应对话术';
    }
}

// ========== 竞品对比分析 ==========
async function generateCompetitorCompare() {
    const competitor = document.getElementById('competitor-select').value;
    const industry = document.getElementById('competitor-industry').value.trim();
    const scenario = document.getElementById('competitor-scenario').value.trim();

    const btn = event.target;
    btn.disabled = true;
    btn.innerHTML = '<i class="fa fa-spinner fa-spin mr-1"></i> 生成中...';

    try {
        const response = await fetch(`${API_BASE_URL}/competitor-compare`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                competitor: competitor,
                industry: industry,
                scenario: scenario,
                identity: currentIdentity,
            })
        });

        if (!response.ok) {
            throw new Error('生成失败');
        }

        const data = await response.json();

        document.getElementById('competitor-content').innerHTML = marked.parse(data.comparison);
        document.getElementById('competitor-result').classList.remove('hidden');
        
        // 如果有当前客户，保存到历史记录
        if (currentCustomerId) {
            const competitor = document.getElementById('competitor-select').value;
            addRecord(currentCustomerId, 'competitor', 
                `竞品对比：${competitor}`, 
                data.comparison);
        }

    } catch (error) {
        console.error('生成竞品对比失败:', error);
        alert('生成失败，请检查后端服务');
    } finally {
        btn.disabled = false;
        btn.innerHTML = '<i class="fa fa-search mr-1"></i> 生成对比分析';
    }
}

// ========== 客户背调 ==========

async function generateResearch() {
    const companyName = document.getElementById('company-name').value.trim();
    const industry = document.getElementById('research-industry').value.trim();
    const position = document.getElementById('research-position').value.trim();
    const focus = document.getElementById('research-focus').value.trim();

    if (!companyName) {
        alert('请输入公司名称');
        return;
    }

    const btn = document.getElementById('research-btn');
    const emptyState = document.getElementById('research-empty');
    const loadingState = document.getElementById('research-loading');
    const resultState = document.getElementById('research-result');

    // 显示加载状态
    btn.disabled = true;
    btn.innerHTML = '<i class="fa fa-spinner fa-spin mr-2"></i> 生成中...';
    emptyState.classList.add('hidden');
    resultState.classList.add('hidden');
    loadingState.classList.remove('hidden');

    // 模拟加载进度文字
    const loadingTexts = [
        '正在收集公司基本信息...',
        '正在分析最新动态与新闻...',
        '正在梳理行业与竞品...',
        '正在挖掘潜在需求...',
        '正在生成拜访策略建议...'
    ];
    let textIndex = 0;
    const loadingInterval = setInterval(() => {
        textIndex = (textIndex + 1) % loadingTexts.length;
        document.getElementById('research-loading-text').textContent = loadingTexts[textIndex];
    }, 1500);

    try {
        const response = await fetch(`${API_BASE_URL}/company-research`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                company_name: companyName,
                industry: industry,
                position: position,
                focus: focus,
                identity: currentIdentity
            })
        });

        if (!response.ok) {
            throw new Error('生成失败');
        }

        const data = await response.json();
        currentResearch = data;

        // 如果有当前客户，保存到历史记录
        if (currentCustomerId) {
            addRecord(currentCustomerId, 'research', `${data.company_name} 背调报告`, data.content);
        }

        // 渲染结果
        document.getElementById('research-title').textContent = `${data.company_name} 背调报告`;
        document.getElementById('research-subtitle').textContent = 
            `${data.industry || '未知行业'} · 生成于 ${new Date().toLocaleString()}`;
        document.getElementById('research-content').innerHTML = marked.parse(data.content);

        // 显示结果
        loadingState.classList.add('hidden');
        resultState.classList.remove('hidden');

    } catch (error) {
        console.error('生成背调报告失败:', error);
        alert('生成失败，请检查后端服务');
        emptyState.classList.remove('hidden');
    } finally {
        clearInterval(loadingInterval);
        loadingState.classList.add('hidden');
        btn.disabled = false;
        btn.innerHTML = '<i class="fa fa-search mr-2"></i> 生成背调报告';
    }
}

function copyResearch() {
    if (!currentResearch) return;
    navigator.clipboard.writeText(currentResearch.content).then(() => {
        alert('已复制到剪贴板');
    });
}

function downloadResearch() {
    if (!currentResearch) return;
    const blob = new Blob([currentResearch.content], { type: 'text/markdown' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${currentResearch.company_name}_背调报告.md`;
    a.click();
    URL.revokeObjectURL(url);
}

// ========== 拜访准备清单 ==========
async function generateVisitChecklist() {
    const company = document.getElementById('visit-company').value.trim();
    const industry = document.getElementById('visit-industry').value.trim();
    const position = document.getElementById('visit-position').value.trim();

    if (!company) {
        alert('请输入客户公司名称');
        return;
    }

    const btn = event.target;
    btn.disabled = true;
    btn.innerHTML = '<i class="fa fa-spinner fa-spin mr-1"></i> 生成中...';

    try {
        const response = await fetch(`${API_BASE_URL}/visit-checklist`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                company: company,
                industry: industry,
                position: position,
                identity: currentIdentity,
            })
        });

        if (!response.ok) {
            throw new Error('生成失败');
        }

        const data = await response.json();

        document.getElementById('visit-content').innerHTML = marked.parse(data.checklist);
        document.getElementById('visit-result').classList.remove('hidden');
        
        // 如果有当前客户，保存到历史记录
        if (currentCustomerId) {
            const company = document.getElementById('visit-company').value.trim();
            addRecord(currentCustomerId, 'checklist', 
                `${company} 拜访准备清单`, 
                data.checklist);
        }

    } catch (error) {
        console.error('生成拜访清单失败:', error);
        alert('生成失败，请检查后端服务');
    } finally {
        btn.disabled = false;
        btn.innerHTML = '<i class="fa fa-list-ul mr-1"></i> 生成准备清单';
    }
}

// ========== 工具函数 ==========
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function setupEventListeners() {
    // 聊天输入框回车发送
    document.getElementById('chat-input').addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
    
    // 调整方案输入框回车
    document.getElementById('adjust-input').addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            adjustSolution();
        }
    });

    // 滚动事件：导航栏效果 + 回到顶部按钮
    window.addEventListener('scroll', () => {
        const nav = document.querySelector('nav');
        const backToTop = document.getElementById('back-to-top');
        const scrollY = window.scrollY;

        // 导航栏滚动效果
        if (scrollY > 50) {
            nav.classList.add('shadow-md');
            nav.style.background = 'rgba(255, 255, 255, 0.95)';
        } else {
            nav.classList.remove('shadow-md');
            nav.style.background = 'rgba(255, 255, 255, 0.8)';
        }

        // 回到顶部按钮显示/隐藏
        if (scrollY > 300) {
            backToTop.classList.remove('opacity-0', 'invisible');
            backToTop.classList.add('opacity-100', 'visible');
        } else {
            backToTop.classList.add('opacity-0', 'invisible');
            backToTop.classList.remove('opacity-100', 'visible');
        }
    });
}

// 回到顶部
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// ========== ROI 计算器 ==========
function calculateROI() {
    const people = parseFloat(document.getElementById('roi-people').value) || 0;
    const salary = parseFloat(document.getElementById('roi-salary').value) || 0;
    const efficiency = parseFloat(document.getElementById('roi-efficiency').value) || 0;
    const cost = parseFloat(document.getElementById('roi-cost').value) || 0; // 万元

    // 计算年节省成本（万元）
    const yearlySaving = (people * salary * 12 * efficiency / 100) / 10000;
    
    // ROI
    const roi = cost > 0 ? ((yearlySaving - cost) / cost * 100) : 0;
    
    // 回报周期（月）
    const monthlySaving = yearlySaving / 12;
    const paybackPeriod = monthlySaving > 0 ? (cost / monthlySaving) : 0;

    // 更新显示
    document.getElementById('roi-saving').textContent = yearlySaving.toFixed(1) + '万';
    document.getElementById('roi-cost-result').textContent = cost.toFixed(1) + '万';
    document.getElementById('roi-ratio').textContent = roi.toFixed(0) + '%';
    document.getElementById('roi-period').textContent = paybackPeriod.toFixed(1) + '个月';

    // 生成话术建议
    let suggestion = '';
    if (paybackPeriod < 1) {
        suggestion = `不到1个月就能回本，当年净赚${(yearlySaving - cost).toFixed(0)}万，性价比超高！`;
    } else if (paybackPeriod < 3) {
        suggestion = `${paybackPeriod.toFixed(1)}个月就能回本，当年投资回报率${roi.toFixed(0)}%，非常划算！`;
    } else if (paybackPeriod < 6) {
        suggestion = `半年内就能收回成本，全年ROI达${roi.toFixed(0)}%，投资价值显著！`;
    } else if (paybackPeriod < 12) {
        suggestion = `不到一年就能回本，长期来看收益可观，值得投入！`;
    } else {
        suggestion = `投资回报周期约${paybackPeriod.toFixed(0)}个月，建议从试点开始逐步推广。`;
    }
    
    document.getElementById('roi-suggestion').textContent = suggestion;
}

// 页面加载时计算一次
document.addEventListener('DOMContentLoaded', () => {
    calculateROI();
});


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
