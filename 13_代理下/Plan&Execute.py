'''欢迎来到LangChain实战课
https://time.geekbang.org/column/intro/100617601
作者 黄佳'''
# 设置OpenAI和SERPAPI的API密钥
from dotenv import load_dotenv  # 用于加载环境变量
load_dotenv()  # 加载 .env 文件中的环境变量

from langchain.chat_models import ChatOpenAI
from langchain_experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner
from langchain.llms import OpenAI
from langchain import SerpAPIWrapper
from langchain.agents.tools import Tool
from langchain import LLMMathChain

search = SerpAPIWrapper()
llm = OpenAI(temperature=0)
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
tools = [
    Tool(
        name = "Search",
        func=search.run,
        description="当你遇到问题时的搜索工具"
    ),
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="用来解决数学问题，计算纽约玫瑰的平均价格，计算100美元能买几束玫瑰"
        # description="当你遇到数学问题时需要用到的工具，比如计算纽约玫瑰的平均价格，计算100美元能买几束玫瑰"
    ),
]
model = ChatOpenAI(temperature=0)
planner = load_chat_planner(model)
executor = load_agent_executor(model, tools, verbose=True)
agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)

agent.run("请帮我计算下：在纽约100美元能买几束玫瑰？，请给出一个大概的数值范围")