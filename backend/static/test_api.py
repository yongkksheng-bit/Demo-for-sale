with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 检查各个API请求是否传递了identity参数
print("=== 检查 API 请求是否传递 identity 参数 ===\n")

# 1. 方案生成
has_solution_identity = "identity: currentIdentity" in content or "identity: identity" in content or "'identity': currentIdentity" in content
print(f"1. 方案生成: {has_solution_identity}")

# 2. 客户背调
has_research_identity = "identity" in content and "company-research" in content
# 更精确地检查
if "generateResearch" in content:
    # 找到这个函数
    idx = content.find("function generateResearch")
    end_idx = content.find("\n}", idx) + 2
    func_content = content[idx:end_idx]
    has_identity_in_research = "identity" in func_content
    print(f"2. 客户背调: {has_identity_in_research}")
else:
    print("2. 客户背调: 函数不存在")

# 3. 对话
has_chat_identity = "chat/stream" in content and "identity" in content
if "function sendMessage" in content:
    idx = content.find("function sendMessage")
    end_idx = content.find("\n}", idx) + 2
    func_content = content[idx:end_idx]
    has_identity_in_chat = "identity" in func_content
    print(f"3. 智能对话: {has_identity_in_chat}")
else:
    print("3. 智能对话: 函数不存在")

# 4. 销售话术
if "function generateSalesScript" in content:
    idx = content.find("function generateSalesScript")
    end_idx = content.find("\n}", idx) + 2
    func_content = content[idx:end_idx]
    has_identity_in_script = "identity" in func_content
    print(f"4. 销售话术: {has_identity_in_script}")
else:
    print("4. 销售话术: 函数不存在")

# 5. 异议处理
if "function handleObjection" in content:
    idx = content.find("function handleObjection")
    end_idx = content.find("\n}", idx) + 2
    func_content = content[idx:end_idx]
    has_identity_in_objection = "identity" in func_content
    print(f"5. 异议处理: {has_identity_in_objection}")
else:
    print("5. 异议处理: 函数不存在")

# 6. 竞品对比
if "function generateCompetitorCompare" in content:
    idx = content.find("function generateCompetitorCompare")
    end_idx = content.find("\n}", idx) + 2
    func_content = content[idx:end_idx]
    has_identity_in_competitor = "identity" in func_content
    print(f"6. 竞品对比: {has_identity_in_competitor}")
else:
    print("6. 竞品对比: 函数不存在")

# 7. 拜访清单
if "function generateVisitChecklist" in content:
    idx = content.find("function generateVisitChecklist")
    end_idx = content.find("\n}", idx) + 2
    func_content = content[idx:end_idx]
    has_identity_in_checklist = "identity" in func_content
    print(f"7. 拜访清单: {has_identity_in_checklist}")
else:
    print("7. 拜访清单: 函数不存在")

# 8. 招标文件分析
if "handleBidFileUpload" in content:
    idx = content.find("function handleBidFileUpload")
    end_idx = content.find("\n}", idx) + 2
    func_content = content[idx:end_idx]
    has_identity_in_bid = "identity" in func_content
    print(f"8. 招标文件分析: {has_identity_in_bid}")
else:
    print("8. 招标文件分析: 函数不存在")
