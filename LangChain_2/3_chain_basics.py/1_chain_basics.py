from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser

load_dotenv()
model =ChatOpenAI(model = "gpt-4o")

prompt_tempalte = ChatPromptTemplate(
    [
         ("system", "You are a comedian who tells jokes about {topic}."),
        ("human", "Tell me {joke_count} jokes."),
    ]
)

chain = prompt_tempalte|model|StrOutputParser()

# Run the chain
result = chain.invoke({"topic": "lawyers", "joke_count": 3})

# Output
print(result)