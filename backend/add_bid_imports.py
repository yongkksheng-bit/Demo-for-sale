with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. 添加 File 和 UploadFile 导入
old_import = "from fastapi import FastAPI"
new_import = "from fastapi import FastAPI, File, UploadFile, Form"
content = content.replace(old_import, new_import, 1)

# 2. 导入 bid_analysis_service
old_service_import = "from services.solution_service import solution_service"
new_service_import = """from services.solution_service import solution_service
from services.bid_service import bid_analysis_service"""
content = content.replace(old_service_import, new_service_import, 1)

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)

print("导入添加完成！")
