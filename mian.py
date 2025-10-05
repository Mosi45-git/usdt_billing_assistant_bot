import asyncio
import logging
import sys
import threading
import traceback
from aiogram import Bot, Dispatcher, html #pip install aiogram
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

proxy = "socks5://127.0.0.1:10808"
proxy_type = "1"

TOKEN = "7328245934:AAERPNBa1XNr1WK2dI1M8gUfjMu7rWjKnHg"
dp = Dispatcher()
bot = dict()
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    #print(f"收到消息@{message.from_user.full_name}[{message.chat.id}]:{message.text}")
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

@dp.message()
async def message(message: Message,bot: Bot) -> None:
    try:
        print(message)
        await message.answer("你好")
    except TypeError:
        await message.answer("触发未知错误")
        traceback.print_exc()

async def aioapp() -> None:
    global bot
    if proxy_type == "1":
        from aiogram.client.session.aiohttp import AiohttpSession # pip install aiohttp-socks
        session = AiohttpSession(proxy=proxy)
        bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML), session=session)
    else:
        bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

def tg_app():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(aioapp())

if __name__ == '__main__':
    threading.Thread(target=tg_app).start()
