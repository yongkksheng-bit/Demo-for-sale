"""
API 数据模型
"""
from pydantic import BaseModel, Field
from typing import List, Optional, Dict


# ========== 通用响应 ==========

class BaseResponse(BaseModel):
    """基础响应"""
    code: int = Field(default=0, description="状态码，0表示成功")
    message: str = Field(default="success", description="消息")
    data: Optional[dict] = Field(default=None, description="数据")


# ========== 问答相关 ==========

class QARequest(BaseModel):
    """问答请求"""
    question: str = Field(..., description="问题", min_length=1)


class QAResponse(BaseModel):
    """问答响应"""
    answer: str = Field(..., description="回答")
    sources: Optional[List[str]] = Field(default=None, description="参考来源")


# ========== 对话相关 ==========

class ChatMessage(BaseModel):
    """聊天消息"""
    role: str = Field(..., description="角色：user/assistant")
    content: str = Field(..., description="内容")


class ChatRequest(BaseModel):
    """对话请求"""
    message: str = Field(..., description="用户消息", min_length=1)
    history: Optional[List[ChatMessage]] = Field(default=None, description="历史消息")
    identity: str = Field(default="云与AI销售", description="销售身份")


class ChatResponse(BaseModel):
    """对话响应"""
    reply: str = Field(..., description="回复")


# ========== 方案生成相关 ==========

class SolutionGenerateRequest(BaseModel):
    """方案生成请求"""
    industry: str = Field(..., description="行业", min_length=1)
    scenario: str = Field(..., description="业务场景/痛点", min_length=1)
    company_size: str = Field(default="中型企业", description="企业规模")
    custom_requirements: str = Field(default="", description="定制化需求")
    identity: str = Field(default="云与AI销售", description="销售身份")


class SolutionGenerateResponse(BaseModel):
    """方案生成响应"""
    industry: str = Field(..., description="行业")
    scenario: str = Field(..., description="业务场景")
    company_size: str = Field(..., description="企业规模")
    content: str = Field(..., description="方案内容（Markdown格式）")
    products: List[str] = Field(default_factory=list, description="涉及的产品")


class SolutionAdjustRequest(BaseModel):
    """方案调整请求"""
    original_content: str = Field(..., description="原始方案内容")
    adjustment: str = Field(..., description="调整要求", min_length=1)


class SolutionAdjustResponse(BaseModel):
    """方案调整响应"""
    content: str = Field(..., description="调整后的方案内容")


# ========== 销售话术相关 ==========

class SalesScriptRequest(BaseModel):
    """销售话术请求"""
    industry: str = Field(..., description="行业", min_length=1)
    scenario: str = Field(..., description="业务场景", min_length=1)


class SalesScriptResponse(BaseModel):
    """销售话术响应"""
    script: str = Field(..., description="销售话术")


class ObjectionRequest(BaseModel):
    """异议处理请求"""
    objection: str = Field(..., description="客户异议", min_length=1)
    industry: str = Field(default="", description="行业")


class ObjectionResponse(BaseModel):
    """异议处理响应"""
    response: str = Field(..., description="应对话术")


# ========== 竞品对比 ==========

class CompetitorCompareRequest(BaseModel):
    """竞品对比请求"""
    competitor: str = Field(..., description="竞品名称", min_length=1)
    industry: str = Field(default="", description="行业")
    scenario: str = Field(default="", description="业务场景")


class CompetitorCompareResponse(BaseModel):
    """竞品对比响应"""
    comparison: str = Field(..., description="对比分析内容")


# ========== 拜访准备清单 ==========

class VisitChecklistRequest(BaseModel):
    """拜访准备清单请求"""
    company: str = Field(..., description="客户公司名称", min_length=1)
    industry: str = Field(default="", description="行业")
    position: str = Field(default="", description="对接人职位")


class VisitChecklistResponse(BaseModel):
    """拜访准备清单响应"""
    checklist: str = Field(..., description="准备清单内容")


class CompanyResearchRequest(BaseModel):
    """客户背调请求"""
    company_name: str = Field(..., description="公司名称", min_length=1)
    industry: str = Field(default="", description="所属行业")
    position: str = Field(default="", description="拜访对象职位")
    focus: str = Field(default="", description="重点关注方向")
    identity: str = Field(default="云与AI销售", description="销售身份")


class CompanyResearchResponse(BaseModel):
    """客户背调响应"""
    company_name: str = Field(..., description="公司名称")
    industry: str = Field(default="", description="行业")
    position: str = Field(default="", description="拜访对象职位")
    content: str = Field(..., description="背调报告内容")


# ========== 行业与场景 ==========

class IndustryInfo(BaseModel):
    """行业信息"""
    name: str = Field(..., description="行业名称")
    icon: str = Field(default="🏭", description="图标")
    scenarios: List[str] = Field(default_factory=list, description="典型场景")


class IndustryListResponse(BaseModel):
    """行业列表响应"""
    industries: List[IndustryInfo] = Field(..., description="行业列表")
