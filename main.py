import asyncio

from gemini_engine import my_ai

from vkbottle import API, Bot, user
from vkbottle.bot import Message
from config import VK_TOKEN
bot = Bot(token = VK_TOKEN)

@bot.on.message(text="Тест") #Правило для хендлера ЛИЧНЫХ сообщений
async def test_handler(message:Message):
    await message.answer("Тест пройден!")

@bot.on.message() # Если вводить что-то, что не выполняет все остальные правила, то будет работать эта функция
async def anyway_handler(message:Message):
    users_info = await bot.api.users.get(user_ids=[message.from_id])
    user = users_info[0]
    text = message.text
    await message.answer(await my_ai(text))

bot.run_forever()