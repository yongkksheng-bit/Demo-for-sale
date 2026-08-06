/**
 * 火山引擎智能方案顾问 - 前端逻辑
 */

// ========== 配置 ==========
const API_BASE_URL = 'https://demo-for-sale.onrender.com/api/v1';

// ========== 状态 ==========
let selectedIndustry = null;
let selectedScenario = null;
let currentSolution = null;
let chatHistory = [];

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
    renderIndustries();
    setupEventListeners();
});

// ========== 页面切换 ==========
function showSection(sectionId) {
    // 隐藏所有 section
    document.querySelectorAll('.section').forEach(s => s.classList.add('hidden'));
    // 显示目标 section
    document.getElementById(sectionId).classList.remove('hidden');
    // 滚动到顶部
    window.scrollTo({ top: 0, behavior: 'smooth' });
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
        '正在匹配火山引擎产品...',
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
        
        const response = await fetch(`${API_BASE_URL}/solution/generate`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                industry: selectedIndustry,
                scenario: selectedScenario,
                company_size: companySize,
                custom_requirements: customReq
            })
        });
        
        if (!response.ok) {
            throw new Error('生成失败');
        }
        
        const data = await response.json();
        currentSolution = data;
        
        // 渲染方案
        renderSolution(data);
        
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

function renderSolution(data) {
    const solutionHeader = document.getElementById('solution-header');
    const solutionMarkdown = document.getElementById('solution-markdown');
    const adjustBar = document.getElementById('adjust-bar');
    const productTags = document.getElementById('product-tags');
    
    // 更新标题
    document.getElementById('solution-title').textContent = `${data.industry}行业解决方案建议书`;
    document.getElementById('solution-subtitle').textContent = `场景：${data.scenario} · 企业规模：${data.company_size}`;
    
    // 产品标签
    productTags.innerHTML = data.products.map(p => `
        <span class="px-3 py-1 bg-primary/10 text-primary text-xs rounded-full">${p}</span>
    `).join('');
    
    // 渲染 Markdown
    solutionMarkdown.innerHTML = marked.parse(data.content);
    
    // 显示
    solutionHeader.classList.remove('hidden');
    solutionMarkdown.classList.remove('hidden');
    adjustBar.classList.remove('hidden');
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
async function sendMessage() {
    const input = document.getElementById('chat-input');
    const message = input.value.trim();
    
    if (!message) return;
    
    // 添加用户消息
    addChatMessage('user', message);
    input.value = '';
    
    // 添加 AI 思考中消息
    const thinkingId = addChatMessage('assistant', '思考中...', true);
    
    try {
        const response = await fetch(`${API_BASE_URL}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                message: message,
                history: chatHistory
            })
        });
        
        if (!response.ok) {
            throw new Error('对话失败');
        }
        
        const data = await response.json();
        
        // 移除思考中消息，添加真实回复
        removeChatMessage(thinkingId);
        addChatMessage('assistant', data.reply);
        
        // 更新历史
        chatHistory.push({ role: 'user', content: message });
        chatHistory.push({ role: 'assistant', content: data.reply });
        
    } catch (error) {
        console.error('对话失败:', error);
        removeChatMessage(thinkingId);
        addChatMessage('assistant', '抱歉，我遇到了一些问题，请稍后再试。');
    }
}

function addChatMessage(role, content, isThinking = false) {
    const messagesContainer = document.getElementById('chat-messages');
    const id = 'msg-' + Date.now();
    
    const messageHtml = role === 'user' 
        ? `
            <div id="${id}" class="flex items-start space-x-3 justify-end">
                <div class="bg-primary text-white rounded-2xl rounded-tr-none px-4 py-3 max-w-[80%]">
                    <p>${escapeHtml(content)}</p>
                </div>
                <div class="w-8 h-8 rounded-full bg-gray-200 flex items-center justify-center flex-shrink-0">
                    <i class="fa fa-user text-gray-500 text-sm"></i>
                </div>
            </div>
        `
        : `
            <div id="${id}" class="flex items-start space-x-3">
                <div class="w-8 h-8 rounded-full bg-gradient-primary flex items-center justify-center flex-shrink-0">
                    <i class="fa fa-bolt text-white text-sm"></i>
                </div>
                <div class="bg-gray-100 rounded-2xl rounded-tl-none px-4 py-3 max-w-[80%]">
                    <div class="text-gray-800 prose prose-sm max-w-none ${isThinking ? 'typing-cursor' : ''}">
                        ${isThinking ? content : marked.parse(content)}
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
                scenario: scenario
            })
        });
        
        if (!response.ok) {
            throw new Error('生成失败');
        }
        
        const data = await response.json();
        
        document.getElementById('script-content').innerHTML = marked.parse(data.script);
        document.getElementById('script-result').classList.remove('hidden');
        
    } catch (error) {
        console.error('生成话术失败:', error);
        alert('生成失败，请检查后端服务');
    } finally {
        btn.disabled = false;
        btn.innerHTML = '<i class="fa fa-magic mr-1"></i> 生成话术';
    }
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
                industry: industry
            })
        });
        
        if (!response.ok) {
            throw new Error('生成失败');
        }
        
        const data = await response.json();
        
        document.getElementById('objection-content').innerHTML = marked.parse(data.response);
        document.getElementById('objection-result').classList.remove('hidden');
        
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
                scenario: scenario
            })
        });

        if (!response.ok) {
            throw new Error('生成失败');
        }

        const data = await response.json();

        document.getElementById('competitor-content').innerHTML = marked.parse(data.comparison);
        document.getElementById('competitor-result').classList.remove('hidden');

    } catch (error) {
        console.error('生成竞品对比失败:', error);
        alert('生成失败，请检查后端服务');
    } finally {
        btn.disabled = false;
        btn.innerHTML = '<i class="fa fa-search mr-1"></i> 生成对比分析';
    }
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
                position: position
            })
        });

        if (!response.ok) {
            throw new Error('生成失败');
        }

        const data = await response.json();

        document.getElementById('visit-content').innerHTML = marked.parse(data.checklist);
        document.getElementById('visit-result').classList.remove('hidden');

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
