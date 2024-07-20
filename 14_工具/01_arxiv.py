# 设置OpenAI API的密钥
from dotenv import load_dotenv  # 用于加载环境变量
load_dotenv()  # 加载 .env 文件中的环境变量

# 导入库
# from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
# from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.agents import  initialize_agent, AgentType, create_react_agent
from langchain_community.agent_toolkits.load_tools import load_tools
# 初始化模型和工具
llm = ChatOpenAI(temperature=0.0)
tools = load_tools(
    ["arxiv"],
)

# 初始化链
agent_chain = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

# 运行链
agent_chain.run("请用中文介绍一下2005.14165这篇论文的主要内容和核心算法?")