"""
火山引擎智能方案顾问 - FastAPI 主入口
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, StreamingResponse
from contextlib import asynccontextmanager
import json

from config import settings
from models.schemas import (
    QARequest, QAResponse,
    ChatRequest, ChatResponse,
    SolutionGenerateRequest, SolutionGenerateResponse,
    SolutionAdjustRequest, SolutionAdjustResponse,
    SalesScriptRequest, SalesScriptResponse,
    ObjectionRequest, ObjectionResponse,
    CompetitorCompareRequest, CompetitorCompareResponse,
    VisitChecklistRequest, VisitChecklistResponse,
    CompanyResearchRequest, CompanyResearchResponse,
    IndustryListResponse, IndustryInfo
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    # 启动时初始化
    print(f"🚀 {settings.APP_NAME} v{settings.APP_VERSION} 启动中...")
    print(f"📦 模型: {settings.ARK_MODEL}")
    
    # 延迟导入，避免启动慢
    from rag.vector_store import vector_store_manager
    from rag.chain import rag_chain
    from services.solution_service import solution_service
    
    # 初始化向量库（如果有数据的话）
    try:
        vector_store_manager.initialize()
        count = vector_store_manager.get_collection_count()
        print(f"📚 向量库文档数: {count}")
    except Exception as e:
        print(f"⚠️ 向量库初始化跳过: {e}")
    
    yield
    # 关闭时清理
    print("👋 应用关闭")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="基于火山方舟大模型的 AI 销售方案生成工具",
    lifespan=lifespan
)

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_ORIGIN] if settings.FRONTEND_ORIGIN != "*" else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========== 基础接口 ==========

@app.get("/api/info")
async def api_info():
    """API 信息"""
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
        "model": settings.ARK_MODEL
    }


@app.get("/health")
async def health_check():
    """健康检查"""
    return {"status": "healthy"}


@app.get("/api/v1/test")
async def test_api():
    """测试接口"""
    return {"message": "API 正常工作", "model": settings.ARK_MODEL}


# ========== 行业与场景 ==========

@app.get("/api/v1/industries", response_model=IndustryListResponse)
async def get_industries():
    """获取行业列表与典型场景"""
    industries = [
        IndustryInfo(
            name="零售电商",
            icon="🛒",
            scenarios=[
                "智能推荐与个性化营销",
                "用户增长与留存",
                "智能客服与对话机器人",
                "商品搜索优化",
                "供应链智能预测"
            ]
        ),
        IndustryInfo(
            name="金融",
            icon="💰",
            scenarios=[
                "智能风控与反欺诈",
                "智能投顾与财富管理",
                "智能客服与营销",
                "文档智能处理",
                "合规与监管科技"
            ]
        ),
        IndustryInfo(
            name="制造",
            icon="🏭",
            scenarios=[
                "工业质检与缺陷检测",
                "预测性维护",
                "生产流程优化",
                "供应链管理",
                "数字孪生与仿真"
            ]
        ),
        IndustryInfo(
            name="汽车",
            icon="🚗",
            scenarios=[
                "智能座舱与车载助手",
                "自动驾驶与车路协同",
                "用户运营与营销",
                "售后智能服务",
                "供应链数字化"
            ]
        ),
        IndustryInfo(
            name="教育",
            icon="📚",
            scenarios=[
                "智能教学与个性化学习",
                "AI 题库与智能批改",
                "智能客服与招生",
                "知识图谱构建",
                "在线教育质量提升"
            ]
        ),
        IndustryInfo(
            name="医疗健康",
            icon="🏥",
            scenarios=[
                "医疗影像智能分析",
                "智能辅助诊断",
                "药物研发加速",
                "患者管理与随访",
                "医疗文档智能处理"
            ]
        ),
        IndustryInfo(
            name="文旅传媒",
            icon="🎬",
            scenarios=[
                "AIGC 内容创作",
                "智能推荐与分发",
                "视频智能处理",
                "数字人与虚拟主播",
                "用户增长与运营"
            ]
        ),
        IndustryInfo(
            name="政企",
            icon="🏛️",
            scenarios=[
                "政务智能客服",
                "城市大脑与智慧城市",
                "数据中台与共享",
                "智能办公与效率提升",
                "安全与应急管理"
            ]
        )
    ]
    
    return IndustryListResponse(industries=industries)


# ========== 问答接口 ==========

@app.post("/api/v1/qa", response_model=QAResponse)
async def qa_endpoint(request: QARequest):
    """智能问答接口"""
    from rag.chain import rag_chain
    
    answer = rag_chain.query(request.question)
    return QAResponse(answer=answer)


# ========== 对话接口 ==========

@app.post("/api/v1/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """多轮对话接口"""
    from rag.chain import rag_chain
    
    history = [msg.model_dump() for msg in (request.history or [])]
    reply = rag_chain.chat(request.message, history, identity=request.identity)
    return ChatResponse(reply=reply)


@app.post("/api/v1/chat/stream")
async def chat_stream_endpoint(request: ChatRequest):
    """流式多轮对话接口（SSE）"""
    from rag.chain import rag_chain
    from fastapi.responses import StreamingResponse
    
    history = [msg.model_dump() for msg in (request.history or [])]
    
    async def generate():
        for chunk in rag_chain.chat_stream(request.message, history, identity=request.identity):
            yield f"data: {chunk}\n\n"
    
    return StreamingResponse(generate(), media_type="text/event-stream")


# ========== 方案生成接口 ==========

@app.post("/api/v1/solution/generate", response_model=SolutionGenerateResponse)
async def generate_solution(request: SolutionGenerateRequest):
    """生成方案建议书"""
    from services.solution_service import solution_service
    
    result = solution_service.generate_solution(
        industry=request.industry,
        scenario=request.scenario,
        company_size=request.company_size,
        custom_requirements=request.custom_requirements,
        identity=request.identity
    )
    
    return SolutionGenerateResponse(**result)


@app.post("/api/v1/solution/generate-stream")
async def generate_solution_stream(request: SolutionGenerateRequest):
    """流式生成方案建议书（SSE）"""
    from services.solution_service import solution_service
    
    async def event_generator():
        for chunk in solution_service.generate_solution_stream(
            industry=request.industry,
            scenario=request.scenario,
            company_size=request.company_size,
            custom_requirements=request.custom_requirements,
            identity=request.identity
        ):
            yield f"data: {json.dumps({'content': chunk})}\n\n"
        # 结束标记
        yield "data: [DONE]\n\n"
    
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"
        }
    )


@app.post("/api/v1/solution/adjust", response_model=SolutionAdjustResponse)
async def adjust_solution(request: SolutionAdjustRequest):
    """调整方案建议书"""
    from services.solution_service import solution_service
    
    result = solution_service.adjust_solution(
        original_solution=request.original_content,
        adjustment=request.adjustment
    )
    
    return SolutionAdjustResponse(content=result)


# ========== 销售话术接口 ==========

@app.post("/api/v1/sales-script", response_model=SalesScriptResponse)
async def generate_sales_script(request: SalesScriptRequest):
    """生成销售话术"""
    from services.solution_service import solution_service
    
    script = solution_service.generate_sales_script(
        industry=request.industry,
        scenario=request.scenario,
        identity=request.identity
    )
    
    return SalesScriptResponse(script=script)


@app.post("/api/v1/sales-script/stream")
async def generate_sales_script_stream(request: SalesScriptRequest):
    """流式生成销售话术（SSE）"""
    from services.solution_service import solution_service
    from fastapi.responses import StreamingResponse
    
    async def generate():
        for chunk in solution_service.generate_sales_script_stream(
            industry=request.industry,
            scenario=request.scenario,
            identity=request.identity
        ):
            yield f"data: {chunk}\n\n"
    
    return StreamingResponse(generate(), media_type="text/event-stream")


@app.post("/api/v1/objection", response_model=ObjectionResponse)
async def handle_objection(request: ObjectionRequest):
    """处理客户异议"""
    from services.solution_service import solution_service
    
    response = solution_service.handle_objection(
        objection=request.objection,
        industry=request.industry,
        identity=request.identity
    )
    
    return ObjectionResponse(response=response)


@app.post("/api/v1/objection/stream")
async def handle_objection_stream(request: ObjectionRequest):
    """流式处理客户异议（SSE）"""
    from services.solution_service import solution_service
    from fastapi.responses import StreamingResponse
    
    async def generate():
        for chunk in solution_service.handle_objection_stream(
            objection=request.objection,
            industry=request.industry,
            identity=request.identity
        ):
            yield f"data: {chunk}\n\n"
    
    return StreamingResponse(generate(), media_type="text/event-stream")


@app.post("/api/v1/competitor-compare", response_model=CompetitorCompareResponse)
async def competitor_compare(request: CompetitorCompareRequest):
    """竞品对比分析"""
    from services.solution_service import solution_service
    
    comparison = solution_service.compare_competitor(
        competitor=request.competitor,
        industry=request.industry,
        scenario=request.scenario,
        identity=request.identity
    )
    
    return CompetitorCompareResponse(comparison=comparison)


@app.post("/api/v1/competitor-compare/stream")
async def competitor_compare_stream(request: CompetitorCompareRequest):
    """流式生成竞品对比分析（SSE）"""
    from services.solution_service import solution_service
    from fastapi.responses import StreamingResponse
    
    async def generate():
        for chunk in solution_service.compare_competitor_stream(
            competitor=request.competitor,
            industry=request.industry,
            scenario=request.scenario,
            identity=request.identity
        ):
            yield f"data: {chunk}\n\n"
    
    return StreamingResponse(generate(), media_type="text/event-stream")


@app.post("/api/v1/visit-checklist", response_model=VisitChecklistResponse)
async def generate_visit_checklist(request: VisitChecklistRequest):
    """生成拜访准备清单"""
    from services.solution_service import solution_service
    
    checklist = solution_service.generate_visit_checklist(
        company=request.company,
        industry=request.industry,
        position=request.position,
        identity=request.identity
    )
    
    return VisitChecklistResponse(checklist=checklist)


@app.post("/api/v1/visit-checklist/stream")
async def generate_visit_checklist_stream(request: VisitChecklistRequest):
    """流式生成拜访准备清单（SSE）"""
    from services.solution_service import solution_service
    from fastapi.responses import StreamingResponse
    
    async def generate():
        for chunk in solution_service.generate_visit_checklist_stream(
            company=request.company,
            industry=request.industry,
            position=request.position,
            identity=request.identity
        ):
            yield f"data: {chunk}\n\n"
    
    return StreamingResponse(generate(), media_type="text/event-stream")


@app.post("/api/v1/company-research", response_model=CompanyResearchResponse)
async def generate_company_research(request: CompanyResearchRequest):
    """生成客户背调报告"""
    from services.solution_service import solution_service
    
    result = solution_service.generate_company_research(
        company_name=request.company_name,
        industry=request.industry,
        position=request.position,
        focus=request.focus,
        identity=request.identity
    )
    
    return CompanyResearchResponse(**result)


# 挂载静态文件（前端页面）- 必须放在所有路由最后
app.mount("/", StaticFiles(directory="static", html=True), name="static")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )
