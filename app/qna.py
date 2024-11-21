from langchain.chains import ConversationChain
# from langchain.chat_models import ChatOpenAI
import openai
from langchain_openai import ChatOpenAI
# from langchain_core.runnables.history import RunnableWithMessageHistory

# # Example of replacement
# chat_history = RunnableWithMessageHistory(llm=chat)


# Initialize ChatOpenAI with the API key
# chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key="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")
chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key="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")
chain = ConversationChain(llm=chat)

def get_response(question):
    return chain.run(question)

def suggest_practice_problems(topic):
    problems = {
        "loops": ["Write a for loop to print numbers from 1 to 10.", "Create a while loop that sums numbers until 100."],
        "functions": ["Write a Python function to calculate the factorial of a number.", "Create a function to reverse a string."],
        "data structures": ["Implement a stack using Python lists.", "Create a program to find duplicates in an array."],
    }
    return problems.get(topic.lower(), ["No problems available for this topic."])
