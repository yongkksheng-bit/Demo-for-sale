with open("app.js", "r", encoding="utf-8") as f:
    content = f.read()

# 搜索 renderPipelineStages
import re
matches = [(m.start(), m.group()) for m in re.finditer(r'renderPipelineStages', content)]
print(f"找到 {len(matches)} 个 renderPipelineStages:")
for pos, match in matches:
    # 显示前后50个字符
    start = max(0, pos - 30)
    end = min(len(content), pos + 50)
    context = content[start:end].replace('\n', '\\n')
    print(f"  位置 {pos}: ...{context}...")
