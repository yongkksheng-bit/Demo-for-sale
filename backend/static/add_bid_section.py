with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# research section 在第995行结束（索引994）
# 在第996行（索引995）插入新的section

insert_idx = 995  # 第996行的位置

bid_section_html = '''
        <!-- 招标文件分析 -->
        <section id="bid-analysis" class="section hidden py-16 bg-gray-50">
            <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-10">
                    <h2 class="text-3xl font-bold text-gray-900 mb-4">招标文件智能分析</h2>
                    <p class="text-gray-500">上传招标文件，AI 自动提炼关键需求、识别风险点、给出应对建议</p>
                </div>
                
                <div id="bid-analysis-content">
                    <!-- 内容由JS动态渲染 -->
                    <div class="flex flex-col items-center justify-center py-20">
                        <div class="w-20 h-20 bg-gray-100 rounded-2xl flex items-center justify-center mb-6">
                            <i class="fa fa-file-text-o text-4xl text-gray-400"></i>
                        </div>
                        <div class="text-gray-600 font-medium mb-2">上传招标文件开始分析</div>
                        <div class="text-gray-400 text-sm mb-6">支持 PDF、Word、TXT 格式，最大 10MB</div>
                        <button onclick="uploadBidDocument()" class="px-6 py-3 bg-gray-900 text-white rounded-xl hover:bg-gray-800 transition-all flex items-center gap-2">
                            <i class="fa fa-upload"></i>
                            选择文件
                        </button>
                    </div>
                </div>
            </div>
        </section>

'''

lines = lines[:insert_idx] + [bid_section_html] + lines[insert_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("招标分析页面添加完成！")
