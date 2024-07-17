from dotenv import load_dotenv
from langchain_openai import  ChatOpenAI
# from langchain_community.chat_models import ChatOpenAI
load_dotenv()
model  = ChatOpenAI(model="gpt-3.5-turbo")

result = model.invoke("what is  the Meaning  of LiFe")


print(result)
print("--------------------------------")

print(result.content)
