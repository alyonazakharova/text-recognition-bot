import argparse
import io
import string

import telebot
import torch
from PIL import Image
from torch.backends import cudnn

from demo import recognitionImage

bot = telebot.TeleBot('5200524703:AAH6uB_jeDK1W0xMCE3CHgNiXIwzJj4p5SU')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет!")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Отправь мне картинку с текстом, а я скажу, что там написано")
    else:
        bot.send_message(message.from_user.id, "Я пока что глупый и ничего не понял. Напиши /help.")


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    imageStream = io.BytesIO(downloaded_file)
    imageFile = Image.open(imageStream)
    imageFile.save('/Users/artem.ustinov/Downloads/deep-text-recognition-benchmark/demo_image/test.jpeg')

    print("imageFile.size=%s", imageFile.size)
    recognitionImage()

    bot.reply_to(message, "Охуеть красиво, только меня еще не научили выдывать в ответ текст с картинки.")


bot.polling(none_stop=True, interval=0)
