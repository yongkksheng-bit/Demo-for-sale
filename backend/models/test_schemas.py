with open("schemas.py", "r", encoding="utf-8") as f:
    content = f.read()

# 检查各个请求模型里有没有 identity 字段
models = [
    ("SolutionGenerateRequest", "方案生成请求"),
    ("CompanyResearchRequest", "客户背调请求"),
    ("ChatRequest", "对话请求"),
    ("SalesScriptRequest", "销售话术请求"),
    ("ObjectionRequest", "异议处理请求"),
    ("CompetitorCompareRequest", "竞品对比请求"),
    ("VisitChecklistRequest", "拜访清单请求"),
]

print("=== Pydantic 模型 identity 字段检查 ===\n")

all_ok = True
for model_name, display_name in models:
    # 找到这个类的定义
    idx = content.find(f"class {model_name}")
    if idx == -1:
        print(f"⚠️  {display_name}: 模型不存在")
        all_ok = False
        continue
    
    # 找到类的结束（下一个 class 或者文件结束）
    next_class = content.find("class ", idx + 10)
    if next_class == -1:
        next_class = len(content)
    
    class_content = content[idx:next_class]
    has_identity = "identity" in class_content
    status = "✅" if has_identity else "❌"
    print(f"{status} {display_name}: identity={'有' if has_identity else '没有'}")
    if not has_identity:
        all_ok = False

print(f"\n{'所有模型都有identity字段！' if all_ok else '还有模型没有identity字段！'}")
