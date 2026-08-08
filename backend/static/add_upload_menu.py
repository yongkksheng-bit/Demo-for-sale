with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找到+号按钮的位置（第191行，索引190）
plus_btn_idx = 190

# 给+号按钮加上onclick事件
old_btn = lines[plus_btn_idx]
new_btn = old_btn.replace("<button ", '<button onclick="toggleUploadMenu()" ')
lines[plus_btn_idx] = new_btn

# 在+号按钮后面加上传菜单（在</button>后面，第193行之前）
upload_menu_html = '''                                    <!-- 上传菜单 -->
                                    <div id="upload-menu" class="absolute left-0 bottom-12 bg-white rounded-xl shadow-lg border border-gray-200 py-2 w-48 hidden z-10">
                                        <button onclick="uploadBidDocument()" class="w-full px-4 py-2.5 text-left text-gray-700 hover:bg-gray-50 flex items-center gap-3">
                                            <i class="fa fa-file-text-o text-gray-400"></i>
                                            <span>上传招标文件</span>
                                        </button>
                                        <div class="border-t border-gray-100 my-1"></div>
                                        <button class="w-full px-4 py-2.5 text-left text-gray-400 flex items-center gap-3 cursor-not-allowed">
                                            <i class="fa fa-user-o text-gray-300"></i>
                                            <span>上传客户资料</span>
                                        </button>
                                        <button class="w-full px-4 py-2.5 text-left text-gray-400 flex items-center gap-3 cursor-not-allowed">
                                            <i class="fa fa-building-o text-gray-300"></i>
                                            <span>上传竞品资料</span>
                                        </button>
                                    </div>
                                    <!-- 隐藏的文件输入 -->
                                    <input type="file" id="bid-file-input" class="hidden" accept=".pdf,.doc,.docx,.txt">
'''

# 在+号按钮的下一行（索引192，也就是</button>的下一行）插入
insert_idx = 193
lines = lines[:insert_idx] + [upload_menu_html] + lines[insert_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("上传菜单HTML添加完成！")
