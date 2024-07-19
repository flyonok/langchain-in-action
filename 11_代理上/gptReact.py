'''欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳'''
# 设置OpenAI和SERPAPI的API密钥
from dotenv import load_dotenv  # 用于加载环境变量
load_dotenv()  # 加载 .env 文件中的环境变量

# 加载所需的库
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
from langchain.tools import Tool
from langchain.chains import LLMMathChain
import langchain
# langchain.debug = True
langchain.verbose = True

# 初始化大模型
llm = OpenAI(temperature=0)

# 初始化 LLMMathChain
math_chain = LLMMathChain(llm=llm)

# 设置工具，包括一个手动定义的 math 工具
tools = load_tools(["serpapi"], llm=llm)
tools.append(Tool(
    name="llm-math",
    func=math_chain.run,
    description="用来解决数学问题"
))

# 初始化Agent
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# 跑起来
try:
    result = agent.run("目前市场上玫瑰花的平均价格是多少？如果我在此基础上加价15%卖出，应该如何定价？")
    print(f'result:{result}')
except ValueError as e:
    print(f"LLMMathChain raised error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
