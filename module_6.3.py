import requests
from threading import Thread
import time

def get_html(link):
    r = requests.get(link)
    print (link, len(r.text))


urls = ['https://news.mail.ru', 'https://pikabu.ru', 'https://www.fontanka.ru',
             'https://www.roblox.com', 'https://rp5.ru']
threads = [Thread(target=get_html, args=[urls[i]]) for i in range(5)]

t1 = time.time()
for i in range(5):
    print(get_html(urls[i]))
print(f'Время последовательного выполнения: {time.time() - t1}')

t2 = time.time()
for start in threads:
    start.start()
for j in threads:
    j.join()
print(f'Время параллельного выполнения: {time.time() - t2}')
    
