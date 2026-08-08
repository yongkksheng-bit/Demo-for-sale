with open("app.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找 renderPipelineStages 函数的位置
pipeline_stages_start = -1
for i, line in enumerate(lines):
    if "function renderPipelineStages" in line:
        pipeline_stages_start = i
        break

print(f"renderPipelineStages 开始于第 {pipeline_stages_start+1} 行")

# 新函数 renderPipelineFunnel 应该在第几行结束？
# 新函数的结构：function renderPipelineFunnel() { ... }
# 找到新函数的结束位置
funnel_start = -1
for i, line in enumerate(lines):
    if "function renderPipelineFunnel" in line:
        funnel_start = i
        break

print(f"renderPipelineFunnel 开始于第 {funnel_start+1} 行")

# 看看第650行到第670行的内容
print("\n第650-670行：")
for i in range(649, min(len(lines), 670)):
    print(f"  {i+1}: {lines[i].rstrip()[:80]}")
