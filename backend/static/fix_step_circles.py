with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 第872行（索引871）
line = lines[871]
print(f"第872行完整内容：")
print(line.strip())

# 提取class
import re
match = re.search(r'class="([^"]*)"', line)
if match:
    cls = match.group(1)
    print(f"\n完整class: {cls}")
    
    # 替换样式
    new_cls = cls.replace("bg-gray-900", "bg-white border border-gray-200 shadow-sm")
    new_cls = new_cls.replace("text-white", "text-gray-900")
    
    print(f"\n新class: {new_cls}")
    
    # 替换这一行
    new_line = line.replace(cls, new_cls)
    lines[871] = new_line
    
    # 再找其他类似的
    count = 1
    for i in range(872, len(lines)):
        if "w-8 h-8 rounded-full bg-gray-900 text-white" in lines[i]:
            old_cls_match = re.search(r'class="([^"]*)"', lines[i])
            if old_cls_match:
                old_cls = old_cls_match.group(1)
                new_cls2 = old_cls.replace("bg-gray-900", "bg-white border border-gray-200 shadow-sm")
                new_cls2 = new_cls2.replace("text-white", "text-gray-900")
                lines[i] = lines[i].replace(old_cls, new_cls2)
                count += 1
    
    print(f"\n总共修改了 {count} 个步骤圆圈")
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.writelines(lines)
