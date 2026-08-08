with open("app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找 renderPipelineStages 函数，它应该在 renderPipelineFunnel 后面
for i, line in enumerate(lines):
    if "function renderPipelineStages" in line:
        print(f"renderPipelineStages 开始于第 {i+1} 行")
        # 往前找10行
        print("\n往前10行：")
        for j in range(max(0, i-10), i):
            print(f"  {j+1}: {lines[j].rstrip()[:80]}")
        break
