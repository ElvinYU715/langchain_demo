#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from utils import DASHSCOPE_API_KEY, BASE_URL


class MovieInfo(BaseModel):
    """电影详情"""
    title: str = Field(..., description="电影标题")
    year: int = Field(..., description="电影发行年份")
    director: str = Field(..., description="电影导演")
    rating: float = Field(..., description="电影评分，10分制")




def main():

    llm = ChatOpenAI(model="deepseek-r1",
                     temperature=0.6,
                     api_key=DASHSCOPE_API_KEY,
                     base_url=BASE_URL)
    
    llm_with_structure = llm.with_structured_output(MovieInfo, include_raw=True)

    res = llm_with_structure.invoke("提供电影《盗墓空间》的基本信息")

    print(res)
    return 0


if __name__=="__main__":
    main()
