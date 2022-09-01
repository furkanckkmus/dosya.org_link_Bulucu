import requests
import random
import threading
import time
from bs4 import BeautifulSoup


def çalıştır():
    while True:
        link = "https://dosya.org/"
        texts = "abcdefghıijklmnoöprsştuüvyzxwqABCDEFGHIJKLMNOPRSTUVYZXWQ0123456789"
        headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36"
        }
        digits = ''.join(random.sample(texts, 3))
        link = link+digits
        time.sleep(random.randrange(10))
        r = requests.get(link, headers=headers)
        # print(link)
        soup = BeautifulSoup(r.content, 'lxml')
        if r.text != "":
            if soup.select_one('title').text != "Error - Dosya Yükle, Dosya Upload":
                print(soup.select_one('title').text, "\n")
                with open("bulunan_linkler.txt", "a") as dosya:
                    yazılacak = str(link), "\t", str(
                        soup.select_one('title').text)
                    dosya.write(str(yazılacak))
                    dosya.write("\n")


for i in range(10):  # Daha hızlı çalışması için burayı artır.
    t1 = threading.Thread(target=çalıştır)
    t1.start()
    print(i, " Thread Başlatıldı..")
