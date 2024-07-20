from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools

llm = ChatOpenAI(temperature=0.0)
tools = load_tools(
    ["arxiv"],
)
prompt = hub.pull("hwchase17/react")

agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
print(agent_executor.invoke({'input':'请用中文介绍一下2005.14165这篇论文的主要内容和核心算法?'}))