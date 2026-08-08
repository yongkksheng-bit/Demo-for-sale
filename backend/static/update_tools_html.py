with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找到销售工具箱区域的开始和结束
tools_start = content.find('id="tools"')
section_end = content.find('</section>', tools_start)
old_tools_section = content[tools_start:section_end + len('</section>')]

# 新的销售工具箱结构
new_tools_section = '''id="tools" class="section hidden py-8">
            <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-10">
                    <h2 class="text-2xl font-bold text-gray-900 mb-2">销售工具箱</h2>
                    <p class="text-gray-500 text-sm">助力销售全流程，提升成单效率</p>
                </div>

                <div class="flex gap-6 bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
                    <!-- 左侧工具列表 -->
                    <div class="w-56 border-r border-gray-100 py-4">
                        <div class="space-y-1 px-3">
                            <button onclick="selectTool('script')" id="tool-script" class="tool-nav-btn w-full text-left px-4 py-3 rounded-xl transition-all hover:bg-gray-50 flex items-center gap-3">
                                <i class="fa fa-microphone text-gray-400 text-lg w-5 text-center"></i>
                                <div>
                                    <div class="font-medium text-gray-900 text-sm">销售话术</div>
                                    <div class="text-xs text-gray-400">生成专业话术</div>
                                </div>
                            </button>
                            <button onclick="selectTool('objection')" id="tool-objection" class="tool-nav-btn w-full text-left px-4 py-3 rounded-xl transition-all hover:bg-gray-50 flex items-center gap-3">
                                <i class="fa fa-shield text-gray-400 text-lg w-5 text-center"></i>
                                <div>
                                    <div class="font-medium text-gray-900 text-sm">异议处理</div>
                                    <div class="text-xs text-gray-400">应对客户疑问</div>
                                </div>
                            </button>
                            <button onclick="selectTool('competitor')" id="tool-competitor" class="tool-nav-btn w-full text-left px-4 py-3 rounded-xl transition-all hover:bg-gray-50 flex items-center gap-3">
                                <i class="fa fa-balance-scale text-gray-400 text-lg w-5 text-center"></i>
                                <div>
                                    <div class="font-medium text-gray-900 text-sm">竞品对比</div>
                                    <div class="text-xs text-gray-400">分析差异化优势</div>
                                </div>
                            </button>
                            <button onclick="selectTool('checklist')" id="tool-checklist" class="tool-nav-btn w-full text-left px-4 py-3 rounded-xl transition-all hover:bg-gray-50 flex items-center gap-3">
                                <i class="fa fa-check-square text-gray-400 text-lg w-5 text-center"></i>
                                <div>
                                    <div class="font-medium text-gray-900 text-sm">拜访清单</div>
                                    <div class="text-xs text-gray-400">拜访准备检查</div>
                                </div>
                            </button>
                            <button onclick="selectTool('roi')" id="tool-roi" class="tool-nav-btn w-full text-left px-4 py-3 rounded-xl transition-all hover:bg-gray-50 flex items-center gap-3">
                                <i class="fa fa-calculator text-gray-400 text-lg w-5 text-center"></i>
                                <div>
                                    <div class="font-medium text-gray-900 text-sm">ROI计算器</div>
                                    <div class="text-xs text-gray-400">投资回报分析</div>
                                </div>
                            </button>
                        </div>
                    </div>

                    <!-- 右侧内容区 -->
                    <div class="flex-1 p-6 min-h-[500px]">
                        <!-- 销售话术 -->
                        <div id="tool-content-script" class="tool-content">
                            <h3 class="text-lg font-semibold text-gray-900 mb-1">销售话术生成</h3>
                            <p class="text-gray-400 text-sm mb-6">根据行业和场景生成专业销售话术</p>
                            
                            <div class="space-y-4 max-w-lg">
                                <div class="grid grid-cols-2 gap-4">
                                    <div>
                                        <label class="block text-sm font-medium text-gray-700 mb-2">行业</label>
                                        <select id="script-industry" class="w-full px-4 py-2.5 border border-gray-200 rounded-xl focus:ring-2 focus:ring-gray-900/10 focus:border-gray-900 outline-none text-sm bg-white">
                                            <option value="零售电商">零售电商</option>
                                            <option value="金融">金融</option>
                                            <option value="制造">制造</option>
                                            <option value="汽车">汽车</option>
                                            <option value="教育">教育</option>
                                            <option value="医疗健康">医疗健康</option>
                                            <option value="文旅传媒">文旅传媒</option>
                                            <option value="政企">政企</option>
                                        </select>
                                    </div>
                                    <div>
                                        <label class="block text-sm font-medium text-gray-700 mb-2">场景</label>
                                        <input id="script-scenario" type="text" placeholder="如：智能推荐" class="w-full px-4 py-2.5 border border-gray-200 rounded-xl focus:ring-2 focus:ring-gray-900/10 focus:border-gray-900 outline-none text-sm">
                                    </div>
                                </div>
                                <button onclick="generateSalesScript()" class="px-6 py-2.5 bg-white border border-gray-200 text-gray-900 rounded-xl hover:bg-gray-50 hover:shadow-md transition-all text-sm font-medium shadow-sm">
                                    <i class="fa fa-magic mr-2"></i>生成话术
                                </button>
                            </div>
                            
                            <div id="script-result" class="hidden mt-6">
                                <div class="bg-gray-50 rounded-xl p-5 max-h-80 overflow-y-auto">
                                    <div id="script-content" class="prose prose-sm max-w-none text-sm"></div>
                                </div>
                            </div>
                        </div>

                        <!-- 异议处理 -->
                        <div id="tool-content-objection" class="tool-content hidden">
                            <h3 class="text-lg font-semibold text-gray-900 mb-1">异议处理助手</h3>
                            <p class="text-gray-400 text-sm mb-6">智能分析客户异议，给出专业回应</p>
                            
                            <div class="space-y-4 max-w-lg">
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-2">客户异议</label>
                                    <textarea id="objection-text" rows="3" placeholder="输入客户提出的异议或疑问..." class="w-full px-4 py-3 border border-gray-200 rounded-xl focus:ring-2 focus:ring-gray-900/10 focus:border-gray-900 outline-none text-sm resize-none"></textarea>
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-2">行业</label>
                                    <select id="objection-industry" class="w-full px-4 py-2.5 border border-gray-200 rounded-xl focus:ring-2 focus:ring-gray-900/10 focus:border-gray-900 outline-none text-sm bg-white">
                                        <option value="零售电商">零售电商</option>
                                        <option value="金融">金融</option>
                                        <option value="制造">制造</option>
                                        <option value="汽车">汽车</option>
                                        <option value="教育">教育</option>
                                        <option value="医疗健康">医疗健康</option>
                                        <option value="文旅传媒">文旅传媒</option>
                                        <option value="政企">政企</option>
                                    </select>
                                </div>
                                <div class="flex flex-wrap gap-2">
                                    <button onclick="setObjection('太贵了')" class="px-3 py-1.5 text-xs bg-gray-50 text-gray-600 rounded-lg hover:bg-gray-100 transition-colors border border-gray-100">太贵了</button>
                                    <button onclick="setObjection('我考虑一下')" class="px-3 py-1.5 text-xs bg-gray-50 text-gray-600 rounded-lg hover:bg-gray-100 transition-colors border border-gray-100">我考虑一下</button>
                                    <button onclick="setObjection('已经用了竞品')" class="px-3 py-1.5 text-xs bg-gray-50 text-gray-600 rounded-lg hover:bg-gray-100 transition-colors border border-gray-100">已经用了竞品</button>
                                    <button onclick="setObjection('和阿里云有啥区别')" class="px-3 py-1.5 text-xs bg-gray-50 text-gray-600 rounded-lg hover:bg-gray-100 transition-colors border border-gray-100">和阿里云有啥区别</button>
                                </div>
                                <button onclick="handleObjection()" class="px-6 py-2.5 bg-white border border-gray-200 text-gray-900 rounded-xl hover:bg-gray-50 hover:shadow-md transition-all text-sm font-medium shadow-sm">
                                    <i class="fa fa-lightbulb-o mr-2"></i>生成回应
                                </button>
                            </div>
                            
                            <div id="objection-result" class="hidden mt-6">
                                <div class="bg-gray-50 rounded-xl p-5 max-h-80 overflow-y-auto">
                                    <div id="objection-content" class="prose prose-sm max-w-none text-sm"></div>
                                </div>
                            </div>
                        </div>

                        <!-- 竞品对比 -->
                        <div id="tool-content-competitor" class="tool-content hidden">
                            <h3 class="text-lg font-semibold text-gray-900 mb-1">竞品对比分析</h3>
                            <p class="text-gray-400 text-sm mb-6">对比分析与竞品的差异化优势</p>
                            
                            <div class="space-y-4 max-w-lg">
                                <div class="grid grid-cols-2 gap-4">
                                    <div>
                                        <label class="block text-sm font-medium text-gray-700 mb-2">竞品名称</label>
                                        <input id="competitor-name" type="text" placeholder="如：阿里云" class="w-full px-4 py-2.5 border border-gray-200 rounded-xl focus:ring-2 focus:ring-gray-900/10 focus:border-gray-900 outline-none text-sm">
                                    </div>
                                    <div>
                                        <label class="block text-sm font-medium text-gray-700 mb-2">行业</label>
                                        <select id="competitor-industry" class="w-full px-4 py-2.5 border border-gray-200 rounded-xl focus:ring-2 focus:ring-gray-900/10 focus:border-gray-900 outline-none text-sm bg-white">
                                            <option value="零售电商">零售电商</option>
                                            <option value="金融">金融</option>
                                            <option value="制造">制造</option>
                                            <option value="汽车">汽车</option>
                                            <option value="教育">教育</option>
                                            <option value="医疗健康">医疗健康</option>
                                            <option value="文旅传媒">文旅传媒</option>
                                            <option value="政企">政企</option>
                                        </select>
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-2">应用场景</label>
                                    <input id="competitor-scenario" type="text" placeholder="如：智能客服" class="w-full px-4 py-2.5 border border-gray-200 rounded-xl focus:ring-2 focus:ring-gray-900/10 focus:border-gray-900 outline-none text-sm">
                                </div>
                                <button onclick="generateCompetitorCompare()" class="px-6 py-2.5 bg-white border border-gray-200 text-gray-900 rounded-xl hover:bg-gray-50 hover:shadow-md transition-all text-sm font-medium shadow-sm">
                                    <i class="fa fa-bar-chart mr-2"></i>生成对比
                                </button>
                            </div>
                            
                            <div id="competitor-result" class="hidden mt-6">
                                <div class="bg-gray-50 rounded-xl p-5 max-h-80 overflow-y-auto">
                                    <div id="competitor-content" class="prose prose-sm max-w-none text-sm"></div>
                                </div>
                            </div>
                        </div>

                        <!-- 拜访清单 -->
                        <div id="tool-content-checklist" class="tool-content hidden">
                            <h3 class="text-lg font-semibold text-gray-900 mb-1">拜访准备清单</h3>
                            <p class="text-gray-400 text-sm mb-6">生成客户拜访前的准备检查清单</p>
                            
                            <div class="space-y-4 max-w-lg">
                                <div class="grid grid-cols-2 gap-4">
                                    <div>
                                        <label class="block text-sm font-medium text-gray-700 mb-2">公司名称</label>
                                        <input id="checklist-company" type="text" placeholder="客户公司名" class="w-full px-4 py-2.5 border border-gray-200 rounded-xl focus:ring-2 focus:ring-gray-900/10 focus:border-gray-900 outline-none text-sm">
                                    </div>
                                    <div>
                                        <label class="block text-sm font-medium text-gray-700 mb-2">行业</label>
                                        <select id="checklist-industry" class="w-full px-4 py-2.5 border border-gray-200 rounded-xl focus:ring-2 focus:ring-gray-900/10 focus:border-gray-900 outline-none text-sm bg-white">
                                            <option value="零售电商">零售电商</option>
                                            <option value="金融">金融</option>
                                            <option value="制造">制造</option>
                                            <option value="汽车">汽车</option>
                                            <option value="教育">教育</option>
                                            <option value="医疗健康">医疗健康</option>
                                            <option value="文旅传媒">文旅传媒</option>
                                            <option value="政企">政企</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="grid grid-cols-2 gap-4">
                                    <div>
                                        <label class="block text-sm font-medium text-gray-700 mb-2">对接人职位</label>
                                        <input id="checklist-position" type="text" placeholder="如：CTO" class="w-full px-4 py-2.5 border border-gray-200 rounded-xl focus:ring-2 focus:ring-gray-900/10 focus:border-gray-900 outline-none text-sm">
                                    </div>
                                </div>
                                <button onclick="generateVisitChecklist()" class="px-6 py-2.5 bg-white border border-gray-200 text-gray-900 rounded-xl hover:bg-gray-50 hover:shadow-md transition-all text-sm font-medium shadow-sm">
                                    <i class="fa fa-list-ul mr-2"></i>生成清单
                                </button>
                            </div>
                            
                            <div id="checklist-result" class="hidden mt-6">
                                <div class="bg-gray-50 rounded-xl p-5 max-h-80 overflow-y-auto">
                                    <div id="checklist-content" class="prose prose-sm max-w-none text-sm"></div>
                                </div>
                            </div>
                        </div>

                        <!-- ROI计算器 -->
                        <div id="tool-content-roi" class="tool-content hidden">
                            <h3 class="text-lg font-semibold text-gray-900 mb-1">ROI 投资回报计算器</h3>
                            <p class="text-gray-400 text-sm mb-6">快速计算方案的投资回报周期</p>
                            
                            <div class="grid grid-cols-2 gap-8">
                                <div class="space-y-4">
                                    <div>
                                        <label class="block text-sm font-medium text-gray-700 mb-2">团队人数</label>
                                        <input id="roi-team-size" type="number" value="50" oninput="calculateROI()" class="w-full px-4 py-2.5 border border-gray-200 rounded-xl focus:ring-2 focus:ring-gray-900/10 focus:border-gray-900 outline-none text-sm">
                                    </div>
                                    <div>
                                        <label class="block text-sm font-medium text-gray-700 mb-2">人均月薪（元）</label>
                                        <input id="roi-salary" type="number" value="15000" oninput="calculateROI()" class="w-full px-4 py-2.5 border border-gray-200 rounded-xl focus:ring-2 focus:ring-gray-900/10 focus:border-gray-900 outline-none text-sm">
                                    </div>
                                    <div>
                                        <label class="block text-sm font-medium text-gray-700 mb-2">效率提升（%）</label>
                                        <input id="roi-efficiency" type="number" value="30" oninput="calculateROI()" class="w-full px-4 py-2.5 border border-gray-200 rounded-xl focus:ring-2 focus:ring-gray-900/10 focus:border-gray-900 outline-none text-sm">
                                    </div>
                                    <div>
                                        <label class="block text-sm font-medium text-gray-700 mb-2">方案年费（元）</label>
                                        <input id="roi-cost" type="number" value="200000" oninput="calculateROI()" class="w-full px-4 py-2.5 border border-gray-200 rounded-xl focus:ring-2 focus:ring-gray-900/10 focus:border-gray-900 outline-none text-sm">
                                    </div>
                                </div>
                                
                                <div class="bg-gray-50 rounded-xl p-5 space-y-4">
                                    <div>
                                        <div class="text-sm text-gray-500 mb-1">年节省成本</div>
                                        <div id="roi-savings" class="text-2xl font-bold text-gray-900">270 万</div>
                                    </div>
                                    <div>
                                        <div class="text-sm text-gray-500 mb-1">投入成本</div>
                                        <div id="roi-investment" class="text-xl font-semibold text-gray-700">20 万</div>
                                    </div>
                                    <div class="border-t border-gray-200 pt-4">
                                        <div class="text-sm text-gray-500 mb-1">ROI 比例</div>
                                        <div id="roi-ratio" class="text-3xl font-bold text-gray-900">1250%</div>
                                    </div>
                                    <div>
                                        <div class="text-sm text-gray-500 mb-1">回报周期</div>
                                        <div id="roi-period" class="text-xl font-semibold text-gray-700">0.9 个月</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>'''

content = content.replace(old_tools_section, new_tools_section)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ 销售工具箱HTML结构已改为左右布局")
