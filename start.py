# -*- coding: cp1251 -*-
import subprocess, urllib.request
import time, datetime,  smtplib
number_of_start = 0
number_of_stop = 0

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Ваше имя пользователя и пароль для учетной записи Google
username = 'andrew3456425@gmail.com'
password = 'ydxq mwqh qddn pzqp'


while True:
    def check_internet_connection():
        try:
            urllib.request.urlopen('http://www.google.com', timeout=1)
            return True
        except urllib.error.URLError:
            return False


    if check_internet_connection():
        print("Интернет-соединение доступно.")
        # Создание объекта MIMEMultipart и настройка заголовков письма
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = 'andrew3456425@gmail.com'
        msg['Subject'] = 'Бот выходит в сеть!'

        # Добавление текста письма
        body = 'Интернет доступен. Бот выходит в сеть'
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        # Подключение к SMTP-серверу Google с использованием двухфакторной аутентификации
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            server.send_message(msg)
            server.quit()
            print('Письмо успешно отправлено')
        except Exception as e:
            print('Ошибка при отправке письма:', str(e))

        process = subprocess.Popen(['python3', 'main.py'])
        number_of_start += 1

        with open("log.txt", 'a') as f:
            f.write(
                f"\n\nЗапуск №{number_of_start}\nВремя запуска: {datetime.datetime.now().strftime('%d.%m.%y %H:%M:%S')}")
        print(f"\n\nЗапуск №{number_of_start}\nВремя запуска: {datetime.datetime.now().strftime('%d.%m.%y %H:%M:%S')}")
        # Создание объекта MIMEMultipart и настройка заголовков письма
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = 'andrew3456425@gmail.com'
        msg['Subject'] = f'Запуск бота №{number_of_start}.Время {datetime.datetime.now().strftime("%d.%m.%y %H:%M:%S")}'

        # Добавление текста письма
        body = f"\n\nЗапуск №{number_of_start}\nВремя запуска: {datetime.datetime.now().strftime('%d.%m.%y %H:%M:%S')}"
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        # Подключение к SMTP-серверу Google с использованием двухфакторной аутентификации
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            server.send_message(msg)
            server.quit()
            print('Письмо успешно отправлено')
        except Exception as e:
            print('Ошибка при отправке письма:', str(e))
        time.sleep(15000)
        process.terminate()
        number_of_stop += 1
        with open("log.txt", 'a') as f:
            f.write(
                f"\n\nОстановка №{number_of_stop}\nВремя остановки: {datetime.datetime.now().strftime('%d.%m.%y %H:%M:%S')}")
            # Создание объекта MIMEMultipart и настройка заголовков письма
            msg = MIMEMultipart()
            msg['From'] = username
            msg['To'] = 'andrew3456425@gmail.com'
            msg['Subject'] = f'Бот остановлен по таймеру №{number_of_start}.Время {datetime.datetime.now().strftime("%d.%m.%y %H:%M:%S")}'

            # Добавление текста письма
            body = 'Бот был остановлен по таймеру. Скоро он перезапуститься, но на случай, проверьте почту'
            msg.attach(MIMEText(body, 'plain', 'utf-8'))

            # Подключение к SMTP-серверу Google с использованием двухфакторной аутентификации
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(username, password)
                server.send_message(msg)
                server.quit()
                print('Письмо успешно отправлено')
            except Exception as e:
                print('Ошибка при отправке письма:', str(e))

    else:

        print("Интернет-соединение недоступно.")
        # Создание объекта MIMEMultipart и настройка заголовков письма
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = 'andrew3456425@gmail.com'
        msg['Subject'] = f'Интернета Нет. {datetime.datetime.now().strftime("%d.%m.%y %H:%M:%S")}'

        # Добавление текста письма
        body = 'Интернета нет, скорее всего, бот отправил сообщения, когда он появился. Пожалуйста проверьте почту'
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        # Подключение к SMTP-серверу Google с использованием двухфакторной аутентификации
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            server.send_message(msg)
            server.quit()
            print('Письмо успешно отправлено')
        except Exception as e:
            print('Ошибка при отправке письма:', str(e))
        process.terminate()
        number_of_stop += 1
        with open("log.txt", 'a') as f:
            f.write(
                f"\n\nОстановка (INTERNET NOT AVAILABLE)№{number_of_stop}\n"
                f"Время остановки: {datetime.datetime.now().strftime('%d.%m.%y %H:%M:%S')}")
            # Создание объекта MIMEMultipart и настройка заголовков письма
            msg = MIMEMultipart()
            msg['From'] = username
            msg['To'] = 'andrew3456425@gmail.com'
            msg['Subject'] = f'Бот остановлен {datetime.datetime.now().strftime("%d.%m.%y %H:%M:%S")}'

            # Добавление текста письма
            body = 'Бот остановлен, потому что нет интернета'
            msg.attach(MIMEText(body, 'plain', 'utf-8'))

            # Подключение к SMTP-серверу Google с использованием двухфакторной аутентификации
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(username, password)
                server.send_message(msg)
                server.quit()
                print('Письмо успешно отправлено')
            except Exception as e:
                print('Ошибка при отправке письма:', str(e))
            time.sleep(12.5)
