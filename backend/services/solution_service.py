"""
方案生成服务 - 核心业务逻辑
"""
from typing import Dict, List, Optional
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from config import settings
from rag.vector_store import vector_store_manager
from services.mock_service import mock_service


class SolutionService:
    """方案生成服务"""
    
    def __init__(self):
        self._llm = None
        self._streaming_llm = None
    
    def _get_llm(self):
        """获取大模型实例（非流式）"""
        if self._llm is None:
            self._llm = ChatOpenAI(
                model=settings.ARK_MODEL,
                openai_api_key=settings.ARK_API_KEY,
                openai_api_base=settings.ARK_BASE_URL,
                temperature=0.7,
                max_tokens=4096,
                request_timeout=120,
                streaming=False
            )
        return self._llm
    
    def _get_streaming_llm(self):
        """获取流式大模型实例"""
        if self._streaming_llm is None:
            self._streaming_llm = ChatOpenAI(
                model=settings.ARK_MODEL,
                openai_api_key=settings.ARK_API_KEY,
                openai_api_base=settings.ARK_BASE_URL,
                temperature=0.7,
                max_tokens=4096,
                request_timeout=120,
                streaming=True
            )
        return self._streaming_llm
    
    def _retrieve_context(self, industry: str, scenario: str, k: int = 8) -> str:
        """检索相关上下文（向量库可选，不可用时返回空）"""
        try:
            query = f"{industry}行业 {scenario} 解决方案"
            docs = vector_store_manager.similarity_search(query, k=k)
            
            context = "\n\n".join([
                f"【{doc.metadata.get('title', '参考资料')}】\n{doc.page_content}"
                for doc in docs
            ])
            return context if context else "（暂无知识库参考，基于通用知识生成）"
        except Exception as e:
            print(f"⚠️  向量库检索失败，使用通用知识生成: {e}")
            return "（向量库暂不可用，基于通用知识生成）"
    
    def generate_solution(self, industry: str, scenario: str, 
                          company_size: str = "中型企业",
                          custom_requirements: str = "") -> Dict:
        """
        生成完整的方案建议书
        
        Args:
            industry: 行业
            scenario: 业务场景/痛点
            company_size: 企业规模
            custom_requirements: 定制化需求
        
        Returns:
            方案建议书字典
        """
        # Mock 模式
        if settings.USE_MOCK:
            print("🔧 使用 Mock 模式生成方案")
            return mock_service.generate_solution(industry, scenario, company_size, custom_requirements)
        
        llm = self._get_llm()
        context = self._retrieve_context(industry, scenario)
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """你是火山引擎的资深解决方案架构师，拥有10年以上企业数字化转型咨询经验。

请根据以下信息，为客户生成一份专业、有说服力的解决方案建议书。

【客户信息】
- 行业：{industry}
- 企业规模：{company_size}
- 业务场景/痛点：{scenario}
- 定制化需求：{custom_requirements}

【参考资料】
{context}

【方案结构要求】
请严格按照以下结构生成方案，使用 Markdown 格式：

# {industry}行业{scenario}解决方案建议书

## 一、行业背景与挑战
- 行业发展趋势
- 企业面临的核心痛点
- 数字化转型的必要性

## 二、解决方案概述
- 方案整体架构
- 核心设计理念
- 方案亮点与优势

## 三、火山引擎产品组合
详细列出使用的火山引擎产品，每个产品包含：
- 产品名称
- 核心功能
- 在本方案中的作用
- 为什么选择这个产品

## 四、方案实施路径
- 分阶段实施计划
- 每个阶段的目标和交付物
- 预计时间周期

## 五、客户价值与ROI
- 业务价值（效率提升、成本降低、收入增长等）
- 技术价值（架构升级、能力沉淀等）
- 投资回报预估

## 六、为什么选择火山引擎
- 技术优势
- 服务能力
- 成功案例
- 生态优势

## 七、下一步行动建议
- 立即可以开展的工作
- 需要客户配合的事项

【火山引擎核心产品清单（请优先从以下产品中选择推荐）】
- 豆包大模型：字节跳动自研大语言模型，支持通用问答、代码生成、内容创作等
- 火山方舟：大模型服务平台，提供模型推理、微调、部署等一站式服务
- 智能推荐引擎：基于字节跳动多年推荐算法积累，提供千人千面个性化推荐
- 智能客服：基于大模型的智能对话机器人，支持多轮对话、知识库问答
- 数据中台：企业级数据治理与分析平台，统一数据管理，打破数据孤岛
- 视觉智能：计算机视觉能力，包括图像识别、OCR、人脸检测、工业质检等
- 语音技术：语音识别、语音合成、声纹识别等全栈语音能力
- 视频云：视频点播、直播、实时音视频、视频剪辑等音视频技术
- 内容安全：文本、图片、视频内容审核，保障内容合规
- 云基础：计算、存储、网络、安全等全栈云基础设施

【要求】
1. 内容要专业、具体、有数据支撑，不要空泛
2. 产品推荐请优先从上述核心产品清单中选择，每个产品说明在方案中的作用
3. 自然地突出火山引擎的差异化优势（字节跳动同款技术、经过亿级用户验证等）
4. 语言要有说服力，像真正的咨询顾问写的
5. 每个部分都要有实质内容，不要敷衍
6. 总字数控制在1800-2500字左右，重点突出，不要啰嗦
7. 使用 Markdown 格式，层级清晰
""")
        ])
        
        chain = prompt | llm | StrOutputParser()
        
        print(f"🎯 正在生成方案: {industry} - {scenario}")
        result = chain.invoke({
            "industry": industry,
            "scenario": scenario,
            "company_size": company_size,
            "custom_requirements": custom_requirements,
            "context": context
        })
        
        return {
            "industry": industry,
            "scenario": scenario,
            "company_size": company_size,
            "content": result,
            "products": self._extract_products(result)
        }
    
    def generate_solution_stream(self, industry: str, scenario: str,
                                  company_size: str = "中型企业",
                                  custom_requirements: str = ""):
        """
        流式生成方案建议书（SSE）
        
        Args:
            industry: 行业
            scenario: 业务场景/痛点
            company_size: 企业规模
            custom_requirements: 定制化需求
        
        Yields:
            每个生成的文本块
        """
        # Mock 模式 - 模拟流式输出
        if settings.USE_MOCK:
            print("🔧 使用 Mock 模式流式生成方案")
            mock_result = mock_service.generate_solution(industry, scenario, company_size, custom_requirements)
            content = mock_result["content"]
            # 模拟逐字输出，每几个字返回一次
            for i in range(0, len(content), 3):
                yield content[i:i+3]
            return
        
        llm = self._get_streaming_llm()
        context = self._retrieve_context(industry, scenario)
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """你是火山引擎的资深解决方案架构师，拥有10年以上企业数字化转型咨询经验。

请根据以下信息，为客户生成一份专业、有说服力的解决方案建议书。

【客户信息】
- 行业：{industry}
- 企业规模：{company_size}
- 业务场景/痛点：{scenario}
- 定制化需求：{custom_requirements}

【参考资料】
{context}

【方案结构要求】
请严格按照以下结构生成方案，使用 Markdown 格式：

# {industry}行业{scenario}解决方案建议书

## 一、行业背景与挑战
- 行业发展趋势
- 企业面临的核心痛点
- 数字化转型的必要性

## 二、解决方案概述
- 方案整体架构
- 核心设计理念
- 方案亮点与优势

## 三、火山引擎产品组合
详细列出使用的火山引擎产品，每个产品包含：
- 产品名称
- 核心功能
- 在本方案中的作用
- 为什么选择这个产品

## 四、方案实施路径
- 分阶段实施计划
- 每个阶段的目标和交付物
- 预计时间周期

## 五、客户价值与ROI
- 业务价值（效率提升、成本降低、收入增长等）
- 技术价值（架构升级、能力沉淀等）
- 投资回报预估

## 六、为什么选择火山引擎
- 技术优势
- 服务能力
- 成功案例
- 生态优势

## 七、下一步行动建议
- 立即可以开展的工作
- 需要客户配合的事项

【火山引擎核心产品清单（请优先从以下产品中选择推荐）】
- 豆包大模型：字节跳动自研大语言模型，支持通用问答、代码生成、内容创作等
- 火山方舟：大模型服务平台，提供模型推理、微调、部署等一站式服务
- 智能推荐引擎：基于字节跳动多年推荐算法积累，提供千人千面个性化推荐
- 智能客服：基于大模型的智能对话机器人，支持多轮对话、知识库问答
- 数据中台：企业级数据治理与分析平台，统一数据管理，打破数据孤岛
- 视觉智能：计算机视觉能力，包括图像识别、OCR、人脸检测、工业质检等
- 语音技术：语音识别、语音合成、声纹识别等全栈语音能力
- 视频云：视频点播、直播、实时音视频、视频剪辑等音视频技术
- 内容安全：文本、图片、视频内容审核，保障内容合规
- 云基础：计算、存储、网络、安全等全栈云基础设施

【要求】
1. 内容要专业、具体、有数据支撑，不要空泛
2. 产品推荐请优先从上述核心产品清单中选择，每个产品说明在方案中的作用
3. 自然地突出火山引擎的差异化优势（字节跳动同款技术、经过亿级用户验证等）
4. 语言要有说服力，像真正的咨询顾问写的
5. 每个部分都要有实质内容，不要敷衍
6. 总字数控制在1800-2500字左右，重点突出，不要啰嗦
7. 使用 Markdown 格式，层级清晰
""")
        ])
        
        chain = prompt | llm | StrOutputParser()
        
        print(f"🎯 正在流式生成方案: {industry} - {scenario}")
        
        # 流式生成
        for chunk in chain.stream({
            "industry": industry,
            "scenario": scenario,
            "company_size": company_size,
            "custom_requirements": custom_requirements,
            "context": context
        }):
            yield chunk
    
    def _extract_products(self, content: str) -> List[str]:
        """从方案内容中提取提到的火山引擎产品"""
        # 产品关键词列表（按优先级排序）
        product_keywords = [
            ("豆包大模型", ["豆包大模型", "豆包", "Doubao", "大模型"]),
            ("火山方舟", ["火山方舟", "方舟", "Ark"]),
            ("智能推荐引擎", ["智能推荐", "推荐引擎", "个性化推荐"]),
            ("智能客服", ["智能客服", "对话机器人", "客服机器人"]),
            ("数据中台", ["数据中台", "数据治理"]),
            ("视觉智能", ["视觉智能", "计算机视觉", "图像识别", "OCR", "工业质检"]),
            ("语音技术", ["语音识别", "语音合成", "语音技术"]),
            ("视频云", ["视频云", "视频点播", "视频直播", "实时音视频"]),
            ("内容安全", ["内容安全", "内容审核"]),
            ("云基础设施", ["云服务器", "对象存储", "云基础"])
        ]
        
        found = []
        for product_name, keywords in product_keywords:
            for keyword in keywords:
                if keyword in content and product_name not in found:
                    found.append(product_name)
                    break
        
        return found
    
    def adjust_solution(self, original_solution: str, adjustment: str) -> str:
        """
        调整已有方案
        
        Args:
            original_solution: 原始方案内容
            adjustment: 调整要求
        
        Returns:
            调整后的方案内容
        """
        # Mock 模式
        if settings.USE_MOCK:
            print("🔧 使用 Mock 模式调整方案")
            return mock_service.adjust_solution(original_solution, adjustment)
        
        llm = self._get_llm()
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """你是火山引擎的解决方案架构师。

请根据用户的调整要求，修改以下方案建议书。

【原始方案】
{original_solution}

【调整要求】
{adjustment}

【要求】
1. 保持原方案的整体结构和专业度
2. 根据调整要求修改相应部分
3. 其他部分保持不变
4. 输出完整的修改后的方案
5. 使用 Markdown 格式
""")
        ])
        
        chain = prompt | llm | StrOutputParser()
        
        result = chain.invoke({
            "original_solution": original_solution,
            "adjustment": adjustment
        })
        
        return result
    
    def generate_sales_script(self, industry: str, scenario: str) -> str:
        """
        生成销售话术
        
        Args:
            industry: 行业
            scenario: 业务场景
        
        Returns:
            销售话术
        """
        # Mock 模式
        if settings.USE_MOCK:
            print("🔧 使用 Mock 模式生成销售话术")
            return mock_service.generate_sales_script(industry, scenario)
        
        llm = self._get_llm()
        context = self._retrieve_context(industry, scenario, k=3)
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """你是火山引擎的金牌销售顾问，擅长挖掘客户需求并给出精准的方案建议。

请为以下场景生成一段专业的销售开场白和需求挖掘话术。

【客户行业】{industry}
【业务场景】{scenario}

【参考资料】
{context}

【话术结构】
1. 开场白（建立信任，引起兴趣）
2. 痛点共鸣（说出客户的痛）
3. 价值铺垫（我们能帮你解决什么）
4. 需求挖掘（引导客户说出更多需求）
5. 下一步行动（约演示/拜访）

【要求】
1. 话术要自然，像真人说的，不要太书面
2. 要有同理心，让客户觉得你懂他
3. 要体现专业性，但不要堆砌术语
4. 总长度控制在500字左右
5. 分点列出，方便销售使用
""")
        ])
        
        chain = prompt | llm | StrOutputParser()
        
        result = chain.invoke({
            "industry": industry,
            "scenario": scenario,
            "context": context
        })
        
        return result
    
    def handle_objection(self, objection: str, industry: str = "") -> str:
        """
        处理客户异议
        
        Args:
            objection: 客户异议
            industry: 行业（可选）
        
        Returns:
            应对话术
        """
        # Mock 模式
        if settings.USE_MOCK:
            print("🔧 使用 Mock 模式处理异议")
            return mock_service.handle_objection(objection, industry)
        
        llm = self._get_llm()
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """你是火山引擎的销售培训专家，精通各种客户异议处理。

请针对以下客户异议，给出专业、有说服力的应对话术。

【客户异议】{objection}
【客户行业】{industry}

【应对策略】
1. 先共情，认可客户的顾虑
2. 再用事实/数据/案例回应
3. 最后转化为机会或下一步行动

【要求】
1. 话术要自然、真诚，不要像背台词
2. 要有理有据，不要强词夺理
3. 要体现火山引擎的优势
4. 分步骤说明应对思路和具体话术
5. 总长度控制在300-500字
""")
        ])
        
        chain = prompt | llm | StrOutputParser()
        
        result = chain.invoke({
            "objection": objection,
            "industry": industry
        })
        
        return result
    
    def compare_competitor(self, competitor: str, industry: str = "", scenario: str = "") -> str:
        """
        竞品对比分析
        
        Args:
            competitor: 竞品名称（阿里云/腾讯云/华为云/AWS等）
            industry: 行业（可选）
            scenario: 场景（可选）
        
        Returns:
            竞品对比分析
        """
        # Mock 模式
        if settings.USE_MOCK:
            print("🔧 使用 Mock 模式竞品对比")
            return self._mock_compare(competitor, industry, scenario)
        
        llm = self._get_llm()
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """你是火山引擎的资深解决方案专家，非常了解各家云厂商的优劣势。

请针对以下竞品，生成一份专业的对比分析，帮助销售了解火山引擎的差异化优势。

【竞品】{competitor}
【行业】{industry}
【场景】{scenario}

【对比结构】
## 一、整体定位对比
- 各自的优势领域和市场定位

## 二、核心能力对比（表格形式）
从以下维度对比：
- 大模型与AI能力
- 计算与存储
- 网络与CDN
- 价格与性价比
- 服务与支持
- 生态与合作伙伴

## 三、火山引擎的差异化优势
- 字节跳动同款技术
- 推荐算法与增长方法论
- 视频与内容技术
- 更灵活的商务政策

## 四、不同场景下的选择建议
- 什么场景选火山引擎更合适
- 什么场景选竞品也可以

## 五、销售话术建议
- 如何突出我们的优势
- 如何应对客户的常见疑问

【要求】
1. 客观公正，不要恶意贬低竞品
2. 突出火山引擎的差异化优势，尤其是字节跳动的技术积累
3. 要有数据和事实支撑，不要空泛
4. 表格要清晰易读
5. 总长度控制在800-1200字
6. 使用 Markdown 格式
""")
        ])
        
        chain = prompt | llm | StrOutputParser()
        
        print(f"⚔️  正在生成竞品对比: 火山引擎 vs {competitor}")
        result = chain.invoke({
            "competitor": competitor,
            "industry": industry if industry else "通用",
            "scenario": scenario if scenario else "通用场景"
        })
        
        return result
    
    def generate_visit_checklist(self, company: str, industry: str = "", position: str = "") -> str:
        """
        生成拜访准备清单
        
        Args:
            company: 客户公司名称
            industry: 行业
            position: 对接人职位
        
        Returns:
            拜访准备清单
        """
        # Mock 模式
        if settings.USE_MOCK:
            print("🔧 使用 Mock 模式生成拜访清单")
            return self._mock_visit_checklist(company, industry, position)
        
        llm = self._get_llm()
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """你是火山引擎的销售总监，经验丰富，擅长指导销售做客户拜访准备。

请为以下客户拜访生成一份详细的准备清单。

【客户公司】{company}
【所属行业】{industry}
【对接人职位】{position}

【清单结构】
## 一、拜访前准备
### 1. 客户调研
- 公司基本情况（规模、业务、发展阶段）
- 行业地位和竞争对手
- 可能的痛点和需求
- 近期的动态和新闻

### 2. 资料准备
- 公司介绍材料
- 相关行业案例
- 产品演示准备
- 报价方案（如需）

### 3. 话术准备
- 开场白
- 需求挖掘问题清单
- 常见异议应对
- 下一步行动引导

## 二、拜访中注意事项
- 破冰技巧
- 倾听技巧
- 需求挖掘方法
- 价值呈现方式

## 三、拜访后跟进
- 当天跟进动作
- 3天内跟进动作
- 长期维护策略

## 四、关键成功因素
- 本次拜访的核心目标
- 成功的衡量标准
- 可能的风险点

【要求】
1. 具体、可执行，不要空泛
2. 站在销售的角度，实用为主
3. 每个部分都要有具体的checklist条目
4. 总长度控制在600-1000字
5. 使用 Markdown 格式，用 checkbox 形式列出清单
""")
        ])
        
        chain = prompt | llm | StrOutputParser()
        
        print(f"📋 正在生成拜访准备清单: {company}")
        result = chain.invoke({
            "company": company,
            "industry": industry if industry else "待确认",
            "position": position if position else "待确认"
        })
        
        return result
    
    def _mock_compare(self, competitor: str, industry: str, scenario: str) -> str:
        """Mock 竞品对比"""
        return f"""# 火山引擎 vs {competitor} 对比分析

## 一、整体定位对比

| 维度 | 火山引擎 | {competitor} |
|------|---------|------------|
| **核心优势** | 字节跳动同款技术，AI与推荐算法领先 | 综合云服务能力强，生态完善 |
| **目标客户** | 互联网、新经济、成长型企业 | 全行业覆盖，大型企业为主 |
| **价格策略** | 更灵活，性价比高 | 标准化定价，量大有优惠 |

## 二、核心能力对比

### 1. 大模型与AI能力
- **火山引擎**：豆包大模型，字节跳动自研，经过抖音/今日头条亿级用户验证，在内容生成、推荐、多模态方面有独特优势
- **{competitor}**：通用大模型能力不错，行业覆盖广，但缺少互联网场景的深度验证

### 2. 推荐与增长
- **火山引擎**：核心优势！字节跳动10年推荐算法积累，抖音/今日头条同款，能直接带来业务增长
- **{competitor}**：有推荐产品，但主要是通用能力，缺少顶级互联网产品的实战验证

### 3. 视频与内容技术
- **火山引擎**：抖音同款视频技术，视频点播、直播、剪辑、特效等能力业界领先
- **{competitor}**：基础视频能力有，但深度和广度不如火山引擎

## 三、火山引擎的差异化优势

1. **字节跳动同款技术** - 经过抖音、今日头条等亿级产品验证的技术，拿来就能用
2. **增长方法论** - 不只是卖产品，还输出字节的增长方法论，帮客户业务增长
3. **更灵活的商务** - 创业公司、成长型企业有更灵活的合作方式
4. **服务更贴心** - 客户成功团队配比更高，响应更快

## 四、销售话术建议

> "王总，其实{competitor}也挺不错的，是行业老大哥了。
>
> 但火山引擎有几个独特的优势，我觉得对您这个场景特别有价值：
>
> 第一，我们的推荐算法是抖音同款的，您也知道抖音的推荐有多厉害。这个不是说我们算法多牛，而是经过了上亿用户、每天万亿级请求的验证，拿来就能用。
>
> 第二，我们不只是卖技术，还会把字节这么多年做增长的方法论分享给您。很多客户跟我们合作后，不只是技术升级了，整个运营思路都提升了。
>
> 第三，我们的服务更灵活。像您这样的成长型企业，我们可以一起探索更适合的合作方式，而不是拿标准套餐给您选。"

---
*注：以上为示例对比，具体以实际情况为准*
"""
    
    def _mock_visit_checklist(self, company: str, industry: str, position: str) -> str:
        """Mock 拜访清单"""
        return f"""# {company} 拜访准备清单

## 一、拜访前准备 ✅

### 1. 客户调研
- [ ] 公司官网和产品体验
- [ ] 最近3个月的新闻和动态
- [ ] 融资情况和发展阶段
- [ ] 竞争对手分析
- [ ] 对接人背景调研（LinkedIn/朋友圈）

### 2. 资料准备
- [ ] 火山引擎公司介绍PPT
- [ ] {industry if industry else "相关"}行业成功案例
- [ ] 产品演示环境准备
- [ ] 初步方案框架
- [ ] 名片/小礼品

### 3. 话术准备
- [ ] 开场白（30秒版本）
- [ ] 需求挖掘5个核心问题
- [ ] 3个最可能的异议应对
- [ ] 下一步行动建议

## 二、拜访中注意事项 🎯

### 1. 破冰（前5分钟）
- [ ] 从对方感兴趣的话题切入
- [ ] 赞美对方公司的某个具体点
- [ ] 找到共同话题

### 2. 需求挖掘（核心）
- [ ] 多问开放式问题
- [ ] 认真倾听，不要急于推销
- [ ] 记笔记，让对方觉得被重视
- [ ] 确认痛点，复述对方的话

### 3. 价值呈现
- [ ] 用案例说话，不要光讲产品
- [ ] 结合对方的痛点讲价值
- [ ] 量化收益，给数字

## 三、拜访后跟进 📞

### 当天（24小时内）
- [ ] 发感谢短信/微信
- [ ] 发会议纪要
- [ ] 发送承诺的资料

### 3天内
- [ ] 电话跟进反馈
- [ ] 推进下一步行动
- [ ] 建立常态化沟通

### 长期
- [ ] 定期分享行业资讯
- [ ] 邀请参加活动
- [ ] 节日问候

## 四、本次拜访目标 🎯

### 主要目标
- [ ] 了解客户真实需求和痛点
- [ ] 建立信任和专业形象
- [ ] 约到下次深入沟通

### 成功标准
- 对方愿意加微信并保持沟通
- 对方主动问了3个以上问题
- 约定了下次沟通时间

---
*祝你拜访顺利！💪*
"""


# 全局单例
solution_service = SolutionService()
