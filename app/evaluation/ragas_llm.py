from langchain_ollama import ChatOllama


def get_ragas_llm():

    return ChatOllama(

        model="qwen2.5:3b",

        temperature=0,

        timeout=300,

    )