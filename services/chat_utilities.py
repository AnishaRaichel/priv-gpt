from llama_index.core.llms import ChatMessage, MessageRole
from llm_factory.get_llm import get_ollama_llm

def get_answer(model_name, chat_history):
    llm = get_ollama_llm(model_name)

    messages = [
        ChatMessage(
            role=MessageRole.SYSTEM,
            content="You are a helpful chat assistant."
        )
    ]

    role_map = {
        "user": MessageRole.USER,
        "assistant": MessageRole.ASSISTANT
    }

    for msg in chat_history:
        role = role_map.get(msg["role"], MessageRole.USER)
        messages.append(
            ChatMessage(role=role, content=msg["content"])
        )

    response = llm.chat(messages=messages)
    return response.message.content