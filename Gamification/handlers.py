from main import bot, dp
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from config import admin_id
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
import loader
import time
from achiv import *
from work_base import *


class Sign_up_users(StatesGroup):
    sign_up_first = State()

class Sign_up_admins(StatesGroup):
    sign_up_first = State()

async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id, text="Бот запущен", reply_markup=menu)


@dp.message_handler(commands=['admin'], state=None)
async def admin_enter(message: types.Message):
    if message.from_user.id == admin_id: await message.answer("Админ панель", reply_markup=menu)
    else: await message.answer("Empty")

@dp.message_handler(commands=['achive'], state=None)
async def admin_enter(message: types.Message):
    if message.from_user.id == admin_id: await bot.send_message(chat_id=admin_id, text=achievement_X001)
    else: await message.answer("Empty")

@dp.message_handler(commands=['start'], state=None)
async def enter_test(message: types.Message):
    await message.answer("Добро пожаловать! Вас приветствует Gamification!", reply_markup=menuQ)


@dp.message_handler(Text(equals=["Регистрация"]), state=None)
async def start_q(message: types.Message):
    #Добавить проверку регистрации
    await message.answer(text="Как к вам обращаться?\nВведите имя/псевдоним", reply_markup=ReplyKeyboardRemove())
    await Sign_up_users.sign_up_first.set()

@dp.message_handler(Text(equals=["Войти"]), state=None)
async def start_q(message: types.Message):
    #Добавить проверку регистрации
    await message.answer(text="Введите код администратора", reply_markup=ReplyKeyboardRemove())
    await Sign_up_admins.sign_up_first.set()


@dp.message_handler(state=Sign_up_users.sign_up_first)
async def answer_q0(message: types.Message, state: FSMContext):
    news_registration = workWithBase.addToBase(str(message.from_user.id), str(message.text))
    if news_registration == True:
        text_registration = str(message.text) + ", добро пожаловать! Далее тут будут появляться ваши достижения."
        await message.answer(text=text_registration, reply_markup=menuQlast)
        await state.finish()
    else:
        await message.answer(text="Вы уже зарегистрированы", reply_markup=menuQlast)
        await state.finish()

@dp.message_handler(state=Sign_up_admins.sign_up_first)
async def answer_q0(message: types.Message, state: FSMContext):
    news_registration = workWithBase.addToBase(str(message.from_user.id), str(message.text))
    if news_registration == True:
        text_registration = str(message.text) + ", добро пожаловать! Это кабинет администратора. Введите /help, чтобы узнать возможности."
        await message.answer(text=text_registration, reply_markup=menuQlast)
        await state.finish()
    else:
        await message.answer(text="Вы уже зарегистрированы", reply_markup=menuQlast)
        await state.finish()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Управление"),
            KeyboardButton(text="Очистить"),
        ],
        [
            KeyboardButton(text="Пользователи"),
            KeyboardButton(text="Создать код"),
        ],
        [
            KeyboardButton(text="/start"),
            KeyboardButton(text="/achive")
        ],
    ],
    resize_keyboard=True
)

menuQ = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="Регистрация")
        ],
        [
        KeyboardButton(text="Войти")
        ],
    ],
    resize_keyboard=True
)

menuQlast = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Войти")
        ],
    ],
    resize_keyboard=True
)

@dp.message_handler(Text(equals=["Управление", "Пользователи", "Создать код", "Очистить"]))
async def admin_control(message: types.Message):
    if message.from_user.id == admin_id:
        if message.text != "Очистить" and message.text != "Пользователи": await message.answer(f"Вы выбрали {message.text}.")
        elif message.text == "Пользователи":
            text_from_takeFromBase = ''
            for i in workWithBase.takeFromBase(): text_from_takeFromBase = text_from_takeFromBase + str(i) + '\n'
            await message.answer(text=str(text_from_takeFromBase))
        elif message.text == "Создать код":

        else: await message.answer("Панель очищена", reply_markup=ReplyKeyboardRemove())

@dp.message_handler()
async def echo(message: Message):
    print(str(message.from_user.username) + " " + str(message.from_user.id) + "\n" + str(message.text))
