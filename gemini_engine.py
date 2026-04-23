from config import GEMINI_API_KEY, PROXY_URL
from google import genai
from google.genai import types

http_options = types.HttpOptions(
    client_args={'proxy': PROXY_URL},
    async_client_args={'proxy': PROXY_URL}
)

client = genai.Client(api_key=GEMINI_API_KEY, http_options=http_options)
context = dict()

async def my_ai(query, id):
    if id not in context:
        context.update({id: []})
    chat = client.aio.chats.create(model='gemini-3.1-flash-lite-preview', history=context[id]) # Модель можете заменить. Список моделей находятся по ссылке:
    content = await chat.send_message(query)
    context[id] = chat.get_history()
    print('Запрос выполнен')
    return content.text

async def delete_chat(id):
    context.pop(id, None)
    return "Чат удалён"