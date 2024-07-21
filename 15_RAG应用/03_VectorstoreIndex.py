# 设置OpenAI的API密钥
from dotenv import load_dotenv  # 用于加载环境变量
load_dotenv()  # 加载 .env 文件中的环境变量
import os
# 导入文档加载器模块，并使用TextLoader来加载文本文件
from langchain.document_loaders import TextLoader,PyPDFLoader
dirName = os.path.abspath(os.path.dirname(__file__))
base_dir = os.path.join(dirName, r"..\02_文档QA系统\OneFlower\易速鲜花员工手册.pdf")
loader = PyPDFLoader(base_dir)

# 使用VectorstoreIndexCreator来从加载器创建索引
from langchain.indexes import VectorstoreIndexCreator
from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
index = VectorstoreIndexCreator(embedding=embeddings).from_loaders([loader])

# 定义查询字符串, 使用创建的索引执行查询
from langchain_openai import OpenAI
# llm = OpenAI(model_name="text-davinci-003",max_tokens=200)
llm = OpenAI(name="gpt4o",max_tokens=200)
query = "易速鲜花的宗旨是？"
result = index.query(query, llm)
print(result) # 打印查询结果


# 替换成你所需要的工具
# from langchain.text_splitter import CharacterTextSplitter
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# from langchain.vectorstores import Chroma

# embeddings = OpenAIEmbeddings()
# index_creator = VectorstoreIndexCreator(
#     vectorstore_cls=Chroma,
#     embedding=OpenAIEmbeddings(),
#     text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# )