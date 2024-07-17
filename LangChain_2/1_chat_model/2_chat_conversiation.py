from dotenv import load_dotenv
import humanfriendly
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
# from langchain_core.messages.ai import 
from langchain_openai import ChatOpenAI
# from openai import RateLimitError

load_dotenv()

model = ChatOpenAI(model='gpt-3.5-turbo')

messages = [
    SystemMessage(content="Give a meaningful answer for the question"),
    HumanMessage(content="What is the meaning of life?")
]
import  sys
try:
    result = model.invoke(messages)
    print(result.content)
except Exception as e:
    raise(e,sys)

## AI Messages



messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
    AIMessage(content="81 divided by 9 is 9."),
    HumanMessage(content="What is 10 times 5?"),
]
