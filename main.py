import logging, datetime, requests
from aiogram import Bot, Dispatcher, types

from aiogram.utils import executor
import asyncio



import os
import requests

files = [
    "Заявка на выезд.doc",
    "Заявка_на_выдачу_разового_пропуска_в_школу (1).pdf",
    "Заявка_на_выдачу_разового_пропуска_в_школу.pdf",
    "Заявление на ПЛАТНОЕ питание.docx",
    "Заявление_на_продление_промежуточной_аттестации.docx",
    "Заявление_об_уходе_ребёнка_начальная_школа.docx",
    "Объяснительная ученика.doc",
    "ПРОТОКОЛ_промежуточной_аттестации.docx",
    "Пропуск на выход продлёнка.docx",
    "заявление на льготное питание.docx",
    "заявление_отсутствие_в_течение_нескольких_дней.docx",
    "заявление_отсутствие_на_несколько_уроков.docx",
    "пропуск на ученика из школы.docx",
    "распис_темат_пятниц.jpg",
    "расписание.jpg"
]
# Базовый URL для загрузки файлов
base_url = "https://raw.githubusercontent.com/Dron3916/school_bot/main/"

# Проверка наличия файлов в папке
existing_files = [file for file in files if os.path.exists(file)]
missing_files = [file for file in files if file not in existing_files]

# Загрузка отсутствующих файлов
for file in missing_files:
    url = base_url + file
    response = requests.get(url)
    with open(file, 'wb') as f:
        f.write(response.content)
        print(f"Файл {file} загружен.")

# Вывод сообщения о файлах, которые уже существуют
for file in existing_files:
    print(f"Файл {file} уже существует и его не нужно загружать.")
    
# Устанавливаем уровень логирования
logging.basicConfig(level=logging.INFO)

# Инициализируем бота и диспетчер
bot = Bot(token='6741255301:AAHLGXx3twvgKNGshv3UE2rZ7m41UF65wOs')
dp = Dispatcher(bot)


# Реакт на старт
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Вывод кнопок
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Классные руководители')
    item2 = types.KeyboardButton('IT служба')
    item3 = types.KeyboardButton('Учебная часть')
    item4 = types.KeyboardButton('ЭЖД')
    item5 = types.KeyboardButton('Кадры')
    item6 = types.KeyboardButton('Завхоз')




    markup.add(item1, item2, item3, item4, item5, item6)

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")



    await bot.send_message("1335412821", f"новый чел {current_time}")
    await bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}.', reply_markup=markup)

# РЕакт на текст сообщения
@dp.message_handler(commands='admin_menu')
async def admin_menu(message: types.Message):

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    await message.reply("Админ меню:" + f"\nТекущее время: {current_time}")
    # РЕакт на текст сообщения
    with open("log.txt", 'r') as f:
        log_for_admin = f.read()

    await message.answer(log_for_admin)


# РЕакт на текст сообщения
@dp.message_handler(content_types=types.ContentType.TEXT)
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Классные руководители':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item2 = types.KeyboardButton('Заявка на выезд')
            item6 = types.KeyboardButton('Расписание звонков')
            item8 = types.KeyboardButton('Питание')
            item9 = types.KeyboardButton('Посещаемость')
            item10 = types.KeyboardButton('График каникул')
            item11 = types.KeyboardButton("Расписание тематических пятниц")
            item12 = types.KeyboardButton("Пропуска")
            item13 = types.KeyboardButton('Объяснительная ученика')
            item14 = types.KeyboardButton('Чек-лист руководителя класса')
            item15 = types.KeyboardButton('Заявления на отсутствие детей')
            item16 = types.KeyboardButton('Назад')
            markup.add(item2, item6, item8, item9, item10, item11, item12, item13, item14, item15, item16)
            await bot.send_message(message.chat.id, 'Пожалуйста', reply_markup=markup)

        elif message.text == 'IT служба':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('заявка на техническое обслуживание')
            item2 = types.KeyboardButton('Назад')
            markup.add(item1, item2)

            await bot.send_message(message.chat.id, 'Пожалуйста', reply_markup=markup)

        elif message.text == 'Учебная часть':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('ОГЭ')
            item2 = types.KeyboardButton('ЕГЭ')
            item3 = types.KeyboardButton('АООП')
            item4 = types.KeyboardButton('АЗ')
            item5 = types.KeyboardButton('Олимпиады')
            item6 = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5, item6)

            await bot.send_message(message.chat.id, 'Пожалуйста', reply_markup=markup)

        elif message.text == 'ЭЖД':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Часто задаваемые вопросы')
            item2 = types.KeyboardButton('Инструкции')
            item3 = types.KeyboardButton('Обращение к администрации ЭЖД')
            item4 = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4)

            await bot.send_message(message.chat.id, 'Пожалуйста', reply_markup=markup)

        elif message.text == 'Кадры':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Кадры школы')
            item2 = types.KeyboardButton('Формы заявлений')
            item3 = types.KeyboardButton('Назад')

            markup.add(item1, item2, item3)
            await bot.send_message(message.chat.id, 'Пожалуйста', reply_markup=markup)

        elif message.text == 'Питание':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Заказ питания')
            item2 = types.KeyboardButton('Фактическое питание')
            item3 = types.KeyboardButton('Заявление на льготное питание')
            item4 = types.KeyboardButton('Заявление на платное питание')
            item5 = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5)
            await bot.send_message(message.chat.id, 'Пожалуйста', reply_markup=markup)

        elif message.text == 'Пропуска':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Пропуск ранний выход')
            item2 = types.KeyboardButton('Пропуск на выход (продлёнка)')
            item3 = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3)
            await bot.send_message(message.chat.id, 'Пожалуйста', reply_markup=markup)

        elif message.text == 'Заявления на отсутствие детей':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Отсутствие на несколько дней')
            item2 = types.KeyboardButton('Отсутствие на несколько уроков')
            item3 = types.KeyboardButton('Заявление об уходе ребёнка (начальная школа)')
            item4 = types.KeyboardButton('Разовый пропуск')
            item5 = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, item4, item5)
            await bot.send_message(message.chat.id, 'Пожалуйста', reply_markup=markup)


        elif message.text == 'АЗ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Протокол промежуточной аттестации')
            item2 = types.KeyboardButton('Заявление на продление промежуточной аттестации')
            item3 = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3)
            await bot.send_message(message.chat.id, 'Пожалуйста', reply_markup=markup)


        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Классные руководители')
            item2 = types.KeyboardButton('IT служба')
            item3 = types.KeyboardButton('Учебная часть')
            item4 = types.KeyboardButton('ЭЖД')
            item5 = types.KeyboardButton('Кадры')
            item6 = types.KeyboardButton('Завхоз')
            markup.add(item1, item2, item3, item4, item5, item6)

            await bot.send_message(message.chat.id, 'Главное меню', reply_markup=markup)

        elif message.text == 'Инструкции':

            await bot.send_message(message.chat.id, r'https://school.mos.ru/help/?ysclid=lnw05yx8bk56927745')

        elif message.text == 'заявка на техническое обслуживание':

            await bot.send_message(message.chat.id,
                             r'https://docs.google.com/forms/d/e/1FAIpQLSfKIzjncmCee-QZmN7nvG-xnD1ReCVNPchpB54GNLwwCRNvaw/viewform?hl=ru')

        elif message.text == 'Часто задаваемые вопросы':
            file = open(
                r"Алгоритм_действий_для_классного_руководителя_Не_можем_зайти_в_дневник.pdf",
                'rb')
            await bot.send_document(message.chat.id, file)

        elif message.text == 'Кадры школы':
            await bot.send_message(message.chat.id,
                             r'https://docs.google.com/forms/d/e/1FAIpQLSefZrf2FHtLejSxkRagASg2u2XFnotu73-9kiMCbGUcQwaSLg/viewform?vc=0&c=0&w=1&flr=0')


        elif message.text == 'Завхоз':
            await bot.send_message(message.chat.id,
                             r'https://docs.google.com/forms/d/e/1FAIpQLSfKhq8BTWiEDXeeWYqSVTygy_yuL2c4B6VIc6yeHmx5r0eyRA/viewform?vc=0&c=0&w=1&flr=0')
            await bot.send_message(message.chat.id, 'Заявка на ремонт')

        elif message.text == 'Формы заявлений':
            await bot.send_message(message.chat.id, r'https://shkid.mskobr.ru/pedagogam/poleznaya-informaciya')


        elif message.text == 'Посещаемость':
            await bot.send_message(message.chat.id,
                             r'https://docs.google.com/forms/d/1KIrCDesvmBDKlLoZcSsdnSvsnBFH58ZdjjropBD0ksg/viewform?edit_requested=true')

        elif message.text == 'Заказ питания':
            await bot.send_message(message.chat.id,
                             r'https://docs.google.com/forms/d/e/1FAIpQLSf8yXf9hUTOKKoo32euqsdFN-0wURujilzDovH0CZ3nsMcdfw/viewform?vc=0&c=0&w=1&flr=0')

        elif message.text == 'Фактическое питание':
            await bot.send_message(message.chat.id,
                             r'https://docs.google.com/forms/d/e/1FAIpQLSf1XHntDAwR5_z6u-XgJMtxfsFsZuqaRguqtKCKzzIAqtFBDQ/viewform?vc=0&c=0&w=1&flr=0')


        elif message.text == 'Обращение к администрации ЭЖД':
            await bot.send_message(message.chat.id, r'https://forms.gle/XVTdiMonmHeW3ds79')

        elif message.text == 'Олимпиады':
            await bot.send_message(message.chat.id, r'https://mos.olimpiada.ru/')
            await bot.send_message(message.chat.id, r'https://vos.olimpiada.ru/')

        elif message.text == 'Расписание звонков':
            photo = open(r"расписание.jpg", 'rb')
            await bot.send_photo(message.chat.id, photo)

        elif message.text == 'АЗ':
            file = open(r"ПРОТОКОЛ_промежуточной_аттестации.docx", "rb")
            await bot.send_document(message.chat.id, file)

        elif message.text == 'График каникул':
            await bot.send_message(message.chat.id,
                             r"https://st.educom.ru/eduoffices/gateways/get_file.php?id=%7BEC27D7CB-B115-B729-8704-9AABFB488527%7D&name=kalend_2023224.pdf")


        elif message.text == 'ОГЭ':
            await bot.send_message(message.chat.id,
                             r"https://docs.google.com/spreadsheets/d/1WoYRWIOUKsDMIds2rjI2tR5GSmZxpyd0-6h0QFZXX2k/edit?usp=sharing")


        elif message.text == 'Расписание тематических пятниц':
            file = open(r"распис_темат_пятниц.jpg", 'rb')
            await bot.send_photo(message.chat.id, file)

        elif message.text == "Пропуск ранний выход":
            file = open(r"пропуск на ученика из школы.docx", 'rb')
            await bot.send_document(message.chat.id, file)

        elif message.text == "Объяснительная ученика":
            file = open(r"Объяснительная ученика.doc", 'rb')
            await bot.send_document(message.chat.id, file)

        elif message.text == "Чек-лист руководителя класса":
            file = open(r"!_Чек_лист_классного_руководителя.docx", 'rb')
            await bot.send_document(message.chat.id, file)

        elif message.text == "Пропуск на выход (продлёнка)":
            file = open(r"Пропуск на выход продлёнка.docx", 'rb')
            await bot.send_document(message.chat.id, file)

        elif message.text == "Отсутствие на несколько дней":
            file = open(r"заявление_отсутствие_в_течение_нескольких_дней.docx", "rb")
            await bot.send_document(message.chat.id, file)

        elif message.text == "Отсутствие на несколько уроков":
            file = open(r"заявление_отсутствие_на_несколько_уроков.docx", "rb")
            await bot.send_document(message.chat.id, file)

        elif message.text == "Заявление об уходе ребёнка (начальная школа)":
            file = open(r"Заявление_об_уходе_ребёнка_начальная_школа.docx", "rb")
            await bot.send_document(message.chat.id, file)

        elif message.text == "Разовый пропуск":
            file = open(r"Заявка_на_выдачу_разового_пропуска_в_школу.pdf", "rb")
            await bot.send_document(message.chat.id, file)

        elif message.text == "Заявка на выезд":
            file = open(r"Заявка на выезд.doc", "rb")
            await bot.send_document(message.chat.id, file)

        elif message.text == "Протокол промежуточной аттестации":
            file = open(r"ПРОТОКОЛ_промежуточной_аттестации.docx", 'rb')
            await bot.send_document(message.chat.id, file)


        elif message.text == "Заявление на продление промежуточной аттестации":
            file = open(r"Заявление_на_продление_промежуточной_аттестации.docx",
                        'rb')
            await bot.send_document(message.chat.id, file)

        elif message.text == "Заявление на льготное питание":
            file = open(r"заявление на льготное питание.docx", 'rb')
            await bot.send_document(message.chat.id, file)

        elif message.text == "Заявление на платное питание":
            file = open(r"Заявление на ПЛАТНОЕ питание.docx", 'rb')
            await bot.send_document(message.chat.id, file)

        elif message.text == 'ЕГЭ':
            await bot.send_message(message.chat.id,
                             r"https://fipi.ru/ege/otkrytyy-bank-zadaniy-ege?ysclid=lptxw1zc1p984380303")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    input()




