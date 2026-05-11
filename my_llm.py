#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from langchain_openai import ChatOpenAI


def main():

    llm = ChatOpenAI(model="deepseek-r1",
                     temperature=0.5,
                     api_key=os.getenv("DASHSCOPE_API_KEY"),
                     base_url=os.getenv("BASE_URL"))
    res = llm.invoke("请简单介绍一下深度学习，在三句话以内")
    print(type(res))
    print(res)

    return 0


if __name__=="__main__":
    main()
