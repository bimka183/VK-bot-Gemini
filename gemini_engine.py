
from config import GEMINI_API_KEY, PROXY_URL
from google import genai
from google.genai import types

http_options = types.HttpOptions(
    client_args={'proxy': PROXY_URL},
    async_client_args={'proxy': PROXY_URL}
)

client = genai.Client(api_key=GEMINI_API_KEY, http_options=http_options)

async def my_ai(query):
    response = await client.aio.models.generate_content(
        model='gemini-3.1-flash-lite-preview', # Модель можете заменить. Список моделей находятся по ссылке:
        contents = query
    )
    print('Запрос выполнен')
    return response.text
