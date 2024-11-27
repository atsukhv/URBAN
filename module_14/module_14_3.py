from itertools import product

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from module_3.module_3_1 import calls

API_TOKEN = ''

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
button_buy = KeyboardButton('Купить')
keyboard.add(button_calculate, button_info, button_buy)

# Создание Inline-клавиатуры
inline_keyboard = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_keyboard.add(button_calories, button_formulas)

inline_keyboard_buy = InlineKeyboardMarkup()
product1 = InlineKeyboardButton('Product1', callback_data='product_buying')
product2 = InlineKeyboardButton('Product2', callback_data='product_buying')
product3 = InlineKeyboardButton('Product3', callback_data='product_buying')
product4 = InlineKeyboardButton('Product4', callback_data='product_buying')
inline_keyboard_buy.add(product1, product2, product3, product4)

@dp.message_handler(lambda message: message.text == 'Купить')
async def get_buying_list(message: types.Message):
    with open('../module_14/photo/кальций.jpg', 'rb') as k_photo:
        await message.answer_photo(photo=k_photo, caption=f'Название: Кальций\n'
                                                          f'Описание: Для костей👍\n'
                                                          f'Цена: 100 рублей')

    with open('../module_14/photo/карнетин.png', 'rb') as l_photo:
        await message.answer_photo(photo=l_photo, caption=f'Название: Карнетин\n'
                                                          f'Описание: Для спорта👍\n'
                                                          f'Цена: 200 рублей')

    with open('../module_14/photo/Колаген.png', 'rb') as ko_photo:
        await message.answer_photo(photo=ko_photo, caption=f'Название: Колаген\n'
                                                           f'Описание: Для кожи👍\n'
                                                           f'Цена: 300 рублей')

    with open('../module_14/photo/с.png', 'rb') as с_photo:
        await message.answer_photo(photo=с_photo, caption=f'Название: Витамин С\n'
                                                          f'Описание: По сути вкусно, и по вкусу вкусно!\n'
                                                          f'Цена: 400 рублей')
    await message.answer(f'Выберите продукт для покупки:', reply_markup=inline_keyboard_buy)


@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer('Вы успешно приобрели продукт!')


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=inline_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer(
        'Формула Миффлина-Сан Жеора:\n\nДля мужчин:\n\nCalories = 10 * weight + 6.25 * height - 5 * age + 5\n\nДля '
        'женщин:\n\nCalories = 10 * weight + 6.25 * height - 5 * age - 161')
    await call.answer()


@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f'Ваша норма калорий: {calories:.2f} ккал.')
    await state.finish()


@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
