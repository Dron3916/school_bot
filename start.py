import subprocess, urllib.request
import time, datetime
kolvo_start = 0
kolvo_stop = 0
while True:




    def check_internet_connection():
        try:
            urllib.request.urlopen('http://www.google.com', timeout=1)
            return True
        except urllib.error.URLError:
            return False


    if check_internet_connection():
        print("Интернет-соединение доступно.")
        process = subprocess.Popen(['python', 'main.py'])
        kolvo_start += 1
        print(f"\n\nЗапуск №{kolvo_start}\nВремя запуска: {datetime.datetime.now().strftime('%d.%m.%y %H:%M:%S')}")
        with open("log.txt", 'a') as f:
            f.write(
                f"\n\nЗапуск №{kolvo_start}\nВремя запуска: {datetime.datetime.now().strftime('%d.%m.%y %H:%M:%S')}")
        time.sleep(300)
        process.terminate()
        kolvo_stop += 1
        with open("log.txt", 'a') as f:
            f.write(
                f"\n\nОстановка №{kolvo_stop}\nВремя остановки: {datetime.datetime.now().strftime('%d.%m.%y %H:%M:%S')}")


    else:
        time.sleep(12.5)
        print("Интернет-соединение недоступно.")
        process.terminate()
        kolvo_stop += 1
        with open("log.txt", 'a') as f:
            f.write(
                f"\n\nОстановка №{kolvo_stop}\nВремя остановки: {datetime.datetime.now().strftime('%d.%m.%y %H:%M:%S')}")
