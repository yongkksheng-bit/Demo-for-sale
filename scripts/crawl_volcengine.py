"""
火山引擎官网文档爬虫
爬取行业解决方案和产品介绍，构建知识库
"""
import os
import re
import time
import json
from typing import List, Dict
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


class VolcengineCrawler:
    """火山引擎文档爬虫"""
    
    def __init__(self, output_dir: str = "./data/raw"):
        self.output_dir = output_dir
        self.base_url = "https://www.volcengine.com"
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
        
        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(os.path.join(output_dir, "solutions"), exist_ok=True)
        os.makedirs(os.path.join(output_dir, "products"), exist_ok=True)
    
    def _get_page(self, url: str) -> BeautifulSoup:
        """获取页面内容"""
        try:
            resp = self.session.get(url, timeout=30)
            resp.raise_for_status()
            return BeautifulSoup(resp.text, "html.parser")
        except Exception as e:
            print(f"❌ 获取页面失败 {url}: {e}")
            return None
    
    def _extract_text(self, soup: BeautifulSoup) -> str:
        """提取页面正文文本"""
        if not soup:
            return ""
        
        # 移除不需要的元素
        for tag in soup.find_all(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()
        
        # 尝试找到主要内容区域
        main_content = soup.find("main") or soup.find("article") or soup.find("div", class_=re.compile(r"content|main|article"))
        
        if main_content:
            text = main_content.get_text(separator="\n", strip=True)
        else:
            text = soup.get_text(separator="\n", strip=True)
        
        # 清理多余空行
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text
    
    def crawl_solutions(self) -> List[Dict]:
        """爬取行业解决方案"""
        print("🔍 开始爬取行业解决方案...")
        
        solutions_url = "https://www.volcengine.com/solutions"
        soup = self._get_page(solutions_url)
        
        if not soup:
            print("❌ 无法获取解决方案页面")
            return []
        
        solutions = []
        
        # 查找所有解决方案链接
        links = soup.find_all("a", href=re.compile(r"/solutions/"))
        
        for link in tqdm(links, desc="爬取解决方案"):
            href = link.get("href", "")
            title = link.get_text(strip=True)
            
            if not href or not title:
                continue
            
            # 构造完整 URL
            if href.startswith("/"):
                url = urljoin(self.base_url, href)
            elif href.startswith("http"):
                url = href
            else:
                continue
            
            # 去重
            if any(s["url"] == url for s in solutions):
                continue
            
            # 获取页面内容
            page_soup = self._get_page(url)
            content = self._extract_text(page_soup)
            
            if len(content) < 100:  # 内容太少跳过
                continue
            
            solution = {
                "title": title,
                "url": url,
                "content": content,
                "category": "行业解决方案",
                "source": "volcengine.com"
            }
            solutions.append(solution)
            
            # 保存到文件
            safe_title = re.sub(r'[\\/:*?"<>|]', '_', title)[:50]
            filepath = os.path.join(self.output_dir, "solutions", f"{safe_title}.json")
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(solution, f, ensure_ascii=False, indent=2)
            
            time.sleep(0.5)  # 礼貌延时
        
        print(f"✅ 爬取完成，共 {len(solutions)} 个解决方案")
        return solutions
    
    def crawl_products(self) -> List[Dict]:
        """爬取产品介绍"""
        print("🔍 开始爬取产品介绍...")
        
        products_url = "https://www.volcengine.com/products"
        soup = self._get_page(products_url)
        
        if not soup:
            print("❌ 无法获取产品页面")
            return []
        
        products = []
        
        # 查找所有产品链接
        links = soup.find_all("a", href=re.compile(r"/product/|/products/"))
        
        for link in tqdm(links, desc="爬取产品"):
            href = link.get("href", "")
            title = link.get_text(strip=True)
            
            if not href or not title or len(title) > 50:
                continue
            
            # 构造完整 URL
            if href.startswith("/"):
                url = urljoin(self.base_url, href)
            elif href.startswith("http") and "volcengine.com" in href:
                url = href
            else:
                continue
            
            # 去重
            if any(p["url"] == url for p in products):
                continue
            
            # 获取页面内容
            page_soup = self._get_page(url)
            content = self._extract_text(page_soup)
            
            if len(content) < 100:
                continue
            
            product = {
                "title": title,
                "url": url,
                "content": content,
                "category": "产品介绍",
                "source": "volcengine.com"
            }
            products.append(product)
            
            # 保存到文件
            safe_title = re.sub(r'[\\/:*?"<>|]', '_', title)[:50]
            filepath = os.path.join(self.output_dir, "products", f"{safe_title}.json")
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(product, f, ensure_ascii=False, indent=2)
            
            time.sleep(0.5)
        
        print(f"✅ 爬取完成，共 {len(products)} 个产品")
        return products
    
    def crawl_all(self):
        """爬取所有内容"""
        print("🚀 开始爬取火山引擎文档...")
        
        solutions = self.crawl_solutions()
        products = self.crawl_products()
        
        # 保存汇总
        all_docs = solutions + products
        summary_path = os.path.join(self.output_dir, "all_documents.json")
        with open(summary_path, "w", encoding="utf-8") as f:
            json.dump(all_docs, f, ensure_ascii=False, indent=2)
        
        print(f"\n🎉 全部爬取完成！")
        print(f"   解决方案: {len(solutions)} 个")
        print(f"   产品介绍: {len(products)} 个")
        print(f"   总计: {len(all_docs)} 个文档")
        print(f"   保存位置: {self.output_dir}")
        
        return all_docs


def main():
    crawler = VolcengineCrawler()
    crawler.crawl_all()


if __name__ == "__main__":
    main()
