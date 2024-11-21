from langchain.chains import ConversationChain
import openai
from langchain_openai import ChatOpenAI
# from langchain_core.runnables.history import RunnableWithMessageHistory

# # Example of replacement
# chat_history = RunnableWithMessageHistory(llm=chat)

# Initialize ChatOpenAI with the API key
chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key="your_openai_api_key")
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
