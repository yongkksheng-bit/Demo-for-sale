with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 检查有没有调用 loadIdentity
has_load_call = "loadIdentity()" in content
print(f"调用 loadIdentity: {has_load_call}")

# 看看在哪里调用的
if has_load_call:
    idx = content.find("loadIdentity()")
    # 看看上下文
    context = content[max(0, idx-100):idx+50]
    print(f"上下文: ...{context}...")
