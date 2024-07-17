from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import  ChatOpenAI

load_dotenv()

model = ChatOpenAI(model = "gpt-3.5-turbo")

print('----------------------------------------------------------------')
template = "tell a joke about the {topic}"
prompt_ = ChatPromptTemplate.from_template(template)
result_prompt   = prompt_.invoke({'topic':'cats'})
print("Result---Prompt")
print(result_prompt)

print("Result --model__answer")
result = model.invoke(result_prompt)# print((model.invoke(result_prompt)).content)
print(result.content)

# PART 2: Prompt with Multiple Placeholders
print("\n----- Prompt with Multiple Placeholders -----\n")
template_multiple = """You are a helpful assistant.
Human: Tell me a {adjective} short story about a {animal}.
Assistant:"""
prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
prompt = prompt_multiple.invoke({"adjective": "funny", "animal": "panda"})

result = model.invoke(prompt)
print(result.content)

# PART 3: Prompt with System and Human Messages (Using Tuples)
print("\n----- Prompt with System and Human Messages (Tuple) -----\n")
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
result = model.invoke(prompt)
print(result.content)

