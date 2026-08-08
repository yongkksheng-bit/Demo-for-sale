with open("chain.py", "r", encoding="utf-8") as f:
    content = f.read()

# 检查 chat 和 chat_stream 函数有没有 identity 参数
functions = [
    ("def chat", "对话"),
    ("def chat_stream", "对话流式"),
]

print("=== RAG 链 identity 参数检查 ===\n")

all_ok = True
for func_name, display_name in functions:
    idx = content.find(func_name)
    if idx == -1:
        print(f"⚠️  {display_name}: 函数不存在")
        all_ok = False
        continue
    
    param_end = content.find("):", idx)
    if param_end == -1:
        print(f"⚠️  {display_name}: 找不到参数结束")
        all_ok = False
        continue
    
    params = content[idx:param_end]
    has_identity = "identity" in params
    status = "✅" if has_identity else "❌"
    print(f"{status} {display_name}: identity={'有' if has_identity else '没有'}")
    if not has_identity:
        all_ok = False

print(f"\n{'对话函数都有identity参数！' if all_ok else '还有对话函数没有identity参数！'}")
