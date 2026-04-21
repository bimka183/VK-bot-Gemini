import os
from dotenv import load_dotenv

# 1. Загружаем данные из файла .env в систему
load_dotenv()

# 2. Вытаскиваем их из системы и сохраняем в переменные
# Если ключа в .env нет, будет возвращено None или стандартное значение
VK_TOKEN = os.getenv("VK_TOKEN")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not VK_TOKEN or not GEMINI_API_KEY:
    print("ОШИБКА: Ключи API не найдены! Проверьте файл .env")
    exit(1)

PROXY_URL = os.getenv("PROXY_URL", "http://127.0.0.1:10809")

CLIENT_ARGS = {'proxy': PROXY_URL}
ASYNC_CLIENT_ARGS = {'proxy': PROXY_URL}