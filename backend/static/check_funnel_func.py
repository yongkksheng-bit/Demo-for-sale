with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 找 renderPipelineFunnel 函数
start = content.find("function renderPipelineFunnel")
if start == -1:
    start = content.find("renderPipelineFunnel")

end = content.find("}", start) + 1
func = content[start:start+2000]  # 取前2000字符
print("=== renderPipelineFunnel 函数（前2000字） ===")
print(func[:1500])
