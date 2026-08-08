with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 找到企业服务销售的按钮，删掉它
# 先找到企业服务销售那一段
start_marker = '<button onclick="selectSalesType(\'企业服务销售\')"'
end_marker = '</button>'

start_idx = content.find(start_marker)
if start_idx != -1:
    # 找到这个button的结束
    end_idx = content.find(end_marker, start_idx) + len(end_marker)
    
    # 还要删掉前面的空行和后面的空行
    # 往前找，找到上一个换行
    while start_idx > 0 and content[start_idx-1] in [' ', '\n', '\r', '\t']:
        start_idx -= 1
    
    # 往后找，找到下一个非空行
    while end_idx < len(content) and content[end_idx] in [' ', '\n', '\r', '\t']:
        end_idx += 1
    
    content = content[:start_idx] + content[end_idx:]
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("企业服务销售选项已删除！")
else:
    print("找不到企业服务销售选项")
