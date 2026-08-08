with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找到 company-research 接口的结束位置
# 找到 @app.post("/api/v1/company-research" 那一行，然后找到下一个 @app 或者函数结束
company_research_idx = -1
for i, line in enumerate(lines):
    if "/api/v1/company-research" in line:
        company_research_idx = i
        break

print(f"company-research 接口在第 {company_research_idx + 1} 行")

# 找到这个函数的结束位置（下一个 @app 或者 def 之前）
end_idx = -1
for i in range(company_research_idx + 1, len(lines)):
    if lines[i].strip().startswith("@app.") or (lines[i].strip().startswith("def ") and not lines[i].strip().startswith("def ")):
        end_idx = i
        break
    # 或者找到静态文件挂载之前
    if "StaticFiles" in lines[i] or "app.mount" in lines[i]:
        end_idx = i
        break

if end_idx == -1:
    end_idx = len(lines) - 10  # 兜底

print(f"在第 {end_idx + 1} 行之前插入新接口")

# 新的接口代码
bid_endpoint = '''
@app.post("/api/v1/bid/analyze")
async def analyze_bid_document(
    file: UploadFile = File(...),
    identity: str = Form("大客户销售")
):
    """
    分析招标文件，提炼关键需求和风险点
    """
    try:
        # 读取文件内容
        file_content = await file.read()
        filename = file.filename
        
        # 调用服务分析
        result = bid_analysis_service.analyze_bid_document(
            file_content=file_content,
            filename=filename,
            identity=identity
        )
        
        return {
            "success": True,
            "message": "分析完成",
            "data": result
        }
        
    except Exception as e:
        print(f"❌ 招标文件分析失败: {e}")
        import traceback
        traceback.print_exc()
        return {
            "success": False,
            "message": f"分析失败: {str(e)}"
        }

'''

# 插入新接口
lines = lines[:end_idx] + [bid_endpoint] + lines[end_idx:]

with open("main.py", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("招标分析接口添加完成！")
