import json
from aiogram.utils.markdown import hbold, hlink
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import time
import requests
from main import get_data, get_result


API_Token = "5870227266:AAFmBhp3S11pL7Xh30qdjsR2o9gJqyXTjG4"
bot = Bot(token=API_Token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['Процессоры', 'Видеокарты', 'Материнские платы', 'Жесткие диски', 'Оперативная память', 'Блоки питания', 'Корпуса', 'Системы охлаждения']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer('Выбеирте категорию', reply_markup=keyboard)

@dp.message_handler(Text(equals='Процессоры'))
async def get_discount_knives(message: types.Message):
    await message.answer('Пожалуйста подождите...')

    get_data(catagory_type=5431)
    get_result()

    with open('data/5_bot_res.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("name"), item.get("link"))}\n' \
               f'{hbold("Цена до скидки: ")}₽{item.get("basePrice")}\n' \
               f'{hbold("Цена после скидки: ")}₽{item.get("salePrice")}🔥\n' \
               f'{hbold("Бонусы: ")}{item.get("bonus")}🍪\n'

        if index % 20 == 0:
            time.sleep(5)

        await message.answer(card)

@dp.message_handler(Text(equals='Видеокарты'))
async def get_discount_knives(message: types.Message):
    await message.answer('Пожалуйста подождите...')

    get_data(catagory_type=5429)
    get_result()

    with open('data/5_bot_res.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("name"), item.get("link"))}\n' \
               f'{hbold("Цена до скидки: ")}₽{item.get("basePrice")}\n' \
               f'{hbold("Цена после скидки: ")}₽{item.get("salePrice")}🔥\n' \
               f'{hbold("Бонусы: ")}{item.get("bonus")}🍪\n'

        if index % 20 == 0:
            time.sleep(5)

        await message.answer(card)

@dp.message_handler(Text(equals='Материнские платы'))
async def get_discount_knives(message: types.Message):
    await message.answer('Пожалуйста подождите...')

    get_data(catagory_type=5432)
    get_result()

    with open('data/5_bot_res.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("name"), item.get("link"))}\n' \
               f'{hbold("Цена до скидки: ")}₽{item.get("basePrice")}\n' \
               f'{hbold("Цена после скидки: ")}₽{item.get("salePrice")}🔥\n' \
               f'{hbold("Бонусы: ")}{item.get("bonus")}🍪\n'

        if index % 20 == 0:
            time.sleep(5)

        await message.answer(card)

@dp.message_handler(Text(equals='Жесткие диски'))
async def get_discount_knives(message: types.Message):
    await message.answer('Пожалуйста подождите...')

    get_data(catagory_type=5436)
    get_result()

    with open('data/5_bot_res.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("name"), item.get("link"))}\n' \
               f'{hbold("Цена до скидки: ")}₽{item.get("basePrice")}\n' \
               f'{hbold("Цена после скидки: ")}₽{item.get("salePrice")}🔥\n' \
               f'{hbold("Бонусы: ")}{item.get("bonus")}🍪\n'

        if index % 20 == 0:
            time.sleep(5)

        await message.answer(card)

@dp.message_handler(Text(equals='Оперативная память'))
async def get_discount_knives(message: types.Message):
    await message.answer('Пожалуйста подождите...')

    get_data(catagory_type=5433)
    get_result()

    with open('data/5_bot_res.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("name"), item.get("link"))}\n' \
               f'{hbold("Цена до скидки: ")}₽{item.get("basePrice")}\n' \
               f'{hbold("Цена после скидки: ")}₽{item.get("salePrice")}🔥\n' \
               f'{hbold("Бонусы: ")}{item.get("bonus")}🍪\n'

        if index % 20 == 0:
            time.sleep(5)

        await message.answer(card)

@dp.message_handler(Text(equals='Блоки питания'))
async def get_discount_knives(message: types.Message):
    await message.answer('Пожалуйста подождите...')

    get_data(catagory_type=5435)
    get_result()

    with open('data/5_bot_res.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("name"), item.get("link"))}\n' \
               f'{hbold("Цена до скидки: ")}₽{item.get("basePrice")}\n' \
               f'{hbold("Цена после скидки: ")}₽{item.get("salePrice")}🔥\n' \
               f'{hbold("Бонусы: ")}{item.get("bonus")}🍪\n'

        if index % 20 == 0:
            time.sleep(5)

        await message.answer(card)

@dp.message_handler(Text(equals='Корпуса'))
async def get_discount_knives(message: types.Message):
    await message.answer('Пожалуйста подождите...')

    get_data(catagory_type=5434)
    get_result()

    with open('data/5_bot_res.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("name"), item.get("link"))}\n' \
               f'{hbold("Цена до скидки: ")}₽{item.get("basePrice")}\n' \
               f'{hbold("Цена после скидки: ")}₽{item.get("salePrice")}🔥\n' \
               f'{hbold("Бонусы: ")}{item.get("bonus")}🍪\n'

        if index % 20 == 0:
            time.sleep(5)

        await message.answer(card)

@dp.message_handler(Text(equals='Системы охлаждения'))
async def get_discount_knives(message: types.Message):
    await message.answer('Пожалуйста подождите...')

    get_data(catagory_type=6127)
    get_result()

    with open('data/5_bot_res.json', encoding='utf-8') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("name"), item.get("link"))}\n' \
               f'{hbold("Цена до скидки: ")}₽{item.get("basePrice")}\n' \
               f'{hbold("Цена после скидки: ")}₽{item.get("salePrice")}🔥\n' \
               f'{hbold("Бонусы: ")}{item.get("bonus")}🍪\n'

        if index % 20 == 0:
            time.sleep(5)

        await message.answer(card)


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()