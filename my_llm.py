#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from langchain_openai import ChatOpenAI
from langchain.chat_models import init_chat_model
from langchain_core.rate_limiters import InMemoryRateLimiter
from utils import DASHSCOPE_API_KEY, BASE_URL


def main():

    rate_limiter = InMemoryRateLimiter(
        requests_per_second= 0.1,  # 没10s允许一个请求
        check_every_n_seconds= 0.1, # 每100ms检查一次是否允许发出请求
        max_bucket_size= 10 # 控制最大突发请求数
    )

    # llm = ChatOpenAI(model="deepseek-r1",
    #                  temperature=1.3,
    #                  api_key=DASHSCOPE_API_KEY),
    #                  base_url=BASE_URL)
    

    # v1.0以后出现的写法
    llm = init_chat_model(
        model="deepseek-r1",
        model_provider="openai",
        temperature=1.3,
        api_key=DASHSCOPE_API_KEY,
        base_url=BASE_URL,
        rate_limiter=rate_limiter)

    for chunk in llm.stream("请简单介绍一下深度学习，在三句话以内"):
        print(chunk.content, end="", flush=True)

    return 0


if __name__=="__main__":
    main()
