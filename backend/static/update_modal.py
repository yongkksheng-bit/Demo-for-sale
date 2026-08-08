with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找到身份列表的div，替换成两级选择
old_start = "<!-- 身份列表 -->"
old_end = "identity-option w-full"

# 先找到模态框的p-6 div，替换整个内容
start_idx = content.find(old_start)
# 找到模态框结束的位置（在底部按钮之前）
end_marker = '<div class="p-6 border-t border-gray-200">'
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    new_content = '''<!-- 身份列表 -->
            <div class="p-6 overflow-y-auto max-h-[65vh]">
                <!-- 第一步：选择行业 -->
                <div class="mb-8">
                    <div class="flex items-center gap-2 mb-4">
                        <span class="w-6 h-6 bg-gray-900 text-white rounded-full flex items-center justify-center text-xs font-bold">1</span>
                        <h4 class="font-semibold text-gray-900">选择行业</h4>
                    </div>
                    <div class="grid grid-cols-2 gap-3">
                        <button onclick="selectIndustry('物流供应链')" class="industry-option w-full text-left px-4 py-3 border border-gray-200 rounded-xl hover:border-gray-900 hover:bg-gray-50 transition-all">
                            <div class="flex items-center gap-3">
                                <span class="text-xl">🚚</span>
                                <span class="font-medium text-gray-900">物流供应链</span>
                            </div>
                        </button>
                        <button onclick="selectIndustry('广告营销')" class="industry-option w-full text-left px-4 py-3 border border-gray-200 rounded-xl hover:border-gray-900 hover:bg-gray-50 transition-all">
                            <div class="flex items-center gap-3">
                                <span class="text-xl">📢</span>
                                <span class="font-medium text-gray-900">广告营销</span>
                            </div>
                        </button>
                        <button onclick="selectIndustry('科技云计算')" class="industry-option w-full text-left px-4 py-3 border border-gray-200 rounded-xl hover:border-gray-900 hover:bg-gray-50 transition-all">
                            <div class="flex items-center gap-3">
                                <span class="text-xl">💻</span>
                                <span class="font-medium text-gray-900">科技/云计算</span>
                            </div>
                        </button>
                        <button onclick="selectIndustry('金融')" class="industry-option w-full text-left px-4 py-3 border border-gray-200 rounded-xl hover:border-gray-900 hover:bg-gray-50 transition-all">
                            <div class="flex items-center gap-3">
                                <span class="text-xl">💰</span>
                                <span class="font-medium text-gray-900">金融</span>
                            </div>
                        </button>
                        <button onclick="selectIndustry('医疗健康')" class="industry-option w-full text-left px-4 py-3 border border-gray-200 rounded-xl hover:border-gray-900 hover:bg-gray-50 transition-all">
                            <div class="flex items-center gap-3">
                                <span class="text-xl">🏥</span>
                                <span class="font-medium text-gray-900">医疗健康</span>
                            </div>
                        </button>
                        <button onclick="selectIndustry('制造业')" class="industry-option w-full text-left px-4 py-3 border border-gray-200 rounded-xl hover:border-gray-900 hover:bg-gray-50 transition-all">
                            <div class="flex items-center gap-3">
                                <span class="text-xl">🏭</span>
                                <span class="font-medium text-gray-900">制造业</span>
                            </div>
                        </button>
                        <button onclick="selectIndustry('零售电商')" class="industry-option w-full text-left px-4 py-3 border border-gray-200 rounded-xl hover:border-gray-900 hover:bg-gray-50 transition-all">
                            <div class="flex items-center gap-3">
                                <span class="text-xl">🛒</span>
                                <span class="font-medium text-gray-900">零售电商</span>
                            </div>
                        </button>
                        <button onclick="selectIndustry('政企')" class="industry-option w-full text-left px-4 py-3 border border-gray-200 rounded-xl hover:border-gray-900 hover:bg-gray-50 transition-all">
                            <div class="flex items-center gap-3">
                                <span class="text-xl">🏛️</span>
                                <span class="font-medium text-gray-900">政企</span>
                            </div>
                        </button>
                    </div>
                </div>
                
                <!-- 第二步：选择销售类型 -->
                <div id="sales-type-section" class="opacity-50 pointer-events-none">
                    <div class="flex items-center gap-2 mb-4">
                        <span id="step2-badge" class="w-6 h-6 bg-gray-300 text-white rounded-full flex items-center justify-center text-xs font-bold">2</span>
                        <h4 class="font-semibold text-gray-900">选择销售类型</h4>
                    </div>
                    <div class="space-y-3">
                        <button onclick="selectSalesType('大客户销售')" class="sales-type-option w-full text-left px-4 py-3 border border-gray-200 rounded-xl hover:border-gray-900 hover:bg-gray-50 transition-all">
                            <div class="flex items-center gap-3">
                                <i class="fa fa-building text-gray-500 w-5 text-center"></i>
                                <div class="flex-1">
                                    <div class="font-medium text-gray-900">大客户销售</div>
                                    <div class="text-sm text-gray-500 mt-0.5">KA销售，负责头部企业客户，项目型销售</div>
                                </div>
                            </div>
                        </button>
                        <button onclick="selectSalesType('渠道销售')" class="sales-type-option w-full text-left px-4 py-3 border border-gray-200 rounded-xl hover:border-gray-900 hover:bg-gray-50 transition-all">
                            <div class="flex items-center gap-3">
                                <i class="fa fa-sitemap text-gray-500 w-5 text-center"></i>
                                <div class="flex-1">
                                    <div class="font-medium text-gray-900">渠道销售</div>
                                    <div class="text-sm text-gray-500 mt-0.5">代理商、合作伙伴、生态体系建设与管理</div>
                                </div>
                            </div>
                        </button>
                        <button onclick="selectSalesType('行业销售')" class="sales-type-option w-full text-left px-4 py-3 border border-gray-200 rounded-xl hover:border-gray-900 hover:bg-gray-50 transition-all">
                            <div class="flex items-center gap-3">
                                <i class="fa fa-industry text-gray-500 w-5 text-center"></i>
                                <div class="flex-1">
                                    <div class="font-medium text-gray-900">行业销售</div>
                                    <div class="text-sm text-gray-500 mt-0.5">垂直行业线深耕，懂行业懂客户</div>
                                </div>
                            </div>
                        </button>
                        <button onclick="selectSalesType('企业服务销售')" class="sales-type-option w-full text-left px-4 py-3 border border-gray-200 rounded-xl hover:border-gray-900 hover:bg-gray-50 transition-all">
                            <div class="flex items-center gap-3">
                                <i class="fa fa-cloud text-gray-500 w-5 text-center"></i>
                                <div class="flex-1">
                                    <div class="font-medium text-gray-900">企业服务销售</div>
                                    <div class="text-sm text-gray-500 mt-0.5">SaaS、软件、企业解决方案</div>
                                </div>
                            </div>
                        </button>
                        <button onclick="selectSalesType('解决方案销售')" class="sales-type-option w-full text-left px-4 py-3 border border-gray-200 rounded-xl hover:border-gray-900 hover:bg-gray-50 transition-all">
                            <div class="flex items-center gap-3">
                                <i class="fa fa-lightbulb-o text-gray-500 w-5 text-center"></i>
                                <div class="flex-1">
                                    <div class="font-medium text-gray-900">解决方案销售</div>
                                    <div class="text-sm text-gray-500 mt-0.5">方案咨询、复杂项目、价值销售</div>
                                </div>
                            </div>
                        </button>
                    </div>
                </div>
            </div>
            
            <!-- 底部确认按钮 -->
'''
    
    # 替换内容
    result = content[:start_idx] + new_content + content[end_idx:]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(result)
    print("HTML更新完成！")
else:
    print(f"找不到位置: start={start_idx}, end={end_idx}")
