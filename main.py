import asyncio

from gemini_engine import my_ai, delete_chat

from vkbottle import API, Bot, user
from vkbottle import Keyboard, KeyboardButtonColor, Text
from vkbottle.bot import Message
from config import VK_TOKEN
bot = Bot(token = VK_TOKEN)

keyboard = Keyboard(one_time=True, inline=False)
keyboard.add(Text("Удалить чат"), color=KeyboardButtonColor.NEGATIVE)
keyboard=keyboard.get_json()

@bot.on.message(text="Удалить чат")
async def Delete_history(message: Message):
    user_id = message.from_id
    await delete_chat(user_id)
    await message.answer("Контекст очищен!", keyboard=keyboard)

@bot.on.message(text="Тест") #Правило для хендлера ЛИЧНЫХ сообщений
async def test_handler(message:Message):
    await message.answer("Тест пройден!")


@bot.on.message() # Если вводить что-то, что не выполняет все остальные правила, то будет работать эта функция
async def anyway_handler(message: Message):
    user_id = message.from_id
    text = message.text
    ai_response = await my_ai(text, user_id)
    print(ai_response)
    await message.answer(ai_response, keyboard=keyboard)

bot.run_forever()