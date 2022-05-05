from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token="5149913065:AAHTUnjXbACBWNeSpcW5CSuT9nmnbeTq0PE")
dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):


# sent_message =  await bot.send_message(chat_id=message.chat.id , text= "Вы сказали: " + message.text ,)
# print(sent_message)
# sent_photo = await bot.send_photo(message.chat.id,
#                                   photo="https://i03.fotocdn.net/s123/76511e5d20d6fc33/public_pin_l/2813715027.jpg")
# print(sent_photo.photo[-1].file_unique_id)


executor.start_polling(dp)
