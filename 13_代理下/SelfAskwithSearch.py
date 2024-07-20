'''欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳'''
# 设置OpenAI和SERPAPI的API密钥
from dotenv import load_dotenv  # 用于加载环境变量
load_dotenv()  # 加载 .env 文件中的环境变量

from langchain import OpenAI, SerpAPIWrapper 
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
import langchain
# langchain.debug = True
langchain.verbose = True

llm = OpenAI(temperature=0)
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Intermediate Answer", 
        func=search.run,
        # description="useful for when you need to ask with search",
        description="当你遇到问题时的搜索工具"
    )
]

# self_ask_with_search = initialize_agent(
#     tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True, handle_parsing_errors=True
# )
self_ask_with_search = initialize_agent(tools, llm, 
                                        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
                                        verbose=True,
                                        handle_parsing_errors=True)
# self_ask_with_search.run("请问使用玫瑰作为国花的国家的是哪个？它的首都的名字是？")
# self_ask_with_search.run("请问使用玫瑰作为国花的国家的是哪个？这个国家的首都的名字是？")
self_ask_with_search.run("请问哪些国家使用玫瑰作为国花？")