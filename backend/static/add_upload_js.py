with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 在身份选择函数后面加上传相关函数
# 找到 loadIdentity 函数结束的位置
marker = "function loadIdentity() {"
idx = content.find(marker)

# 找到 loadIdentity 函数结束的 }
end_idx = content.find("\n}\n", idx) + 3

# 新的上传相关函数
upload_functions = '''

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
'''

# 插入到 loadIdentity 函数后面
new_content = content[:end_idx] + upload_functions + content[end_idx:]

with open("app.js", "w", encoding="utf-8") as f:
    f.write(new_content)

print("上传功能JS添加完成！")
