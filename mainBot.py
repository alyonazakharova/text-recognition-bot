from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from demo import recognize_image

bot = Bot(token='5200524703:AAH6uB_jeDK1W0xMCE3CHgNiXIwzJj4p5SU')
dp = Dispatcher(bot)


@dp.message_handler(content_types=['text'])
async def get_text_messages(message: types.Message):
    if message.text == "Привет":
        await message.answer("Привет!")
    elif message.text == "/help":
        await message.answer("Отправь мне картинку с текстом, а я скажу, что там написано!")
    else:
        await message.answer("Я ничего не понимаю. Напиши /help.")


@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message: types.Message):
    # /Users/artem.ustinov/Downloads/deep-text-recognition-benchmark/demo_image/test.jpeg
    await message.photo[-1].download('/Users/artem.ustinov/Documents/OLENA/text-recognition-bot/demo_image/test.jpeg')

    await message.answer("Секундочку, надо немного подумать.")

    result = recognize_image()
    await message.reply(f'Думаю, тут написано {result[0]} с точностью' + f'\t{result[1]:0.4f}')


if __name__ == "__main__":
    executor.start_polling(dp)
