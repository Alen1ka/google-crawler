import requests
from bs4 import BeautifulSoup

# сохраним нашу ссылку в перменную
url = 'https://www.google.com/search?q=купить+биткоин'
# начало для 2-10 страниц
split_url = 'https://www.google.com'
# создадим массив для ссылок и переменную, обозначающую номер страницы
links = []
page = 0

# проходим по первым десяти страницам и выводим ссылки
for page in range(10):
    # отправим get()-запрос на сайт и сохраним полученное в переменную response
    response = requests.get(url)
    # воспользуемся BeautifulSoup и отдадим ему response
    # указав в кавычках как он нам поможет "html.parser"
    soup = BeautifulSoup(response.text, 'html.parser')
    # воспользуемся функцией поиска из библеотеки BeautifulSoup4
    # она возьмёт теги divs в коде страницы запроса и в них возьмём теги a
    for divs in soup.find_all("div", class_="kCrYT"):
        for a in divs.find_all("a"):
            # если тег a не содержит тега span, то берём ссылку
            span = a.find('span')
            if span is None:
                href = a.get('href')
                # удаляем из начала ссылки часть "/url?q="
                deleted_start = href[7:]

                # для вывода ссылки только один раз объявим переменную output
                output = 0
                # для вывода правильной ссылки идём по буквам в ссылке
                # и удаляем всё что есть после &
                number_of_letters = 0
                print_letters = []
                for letter in deleted_start:
                    if letter == "&" and output != 1:
                        link = "".join(print_letters)  # строка из списка
                        output = +1
                        links.append(link)
                    else:
                        print_letters.append(letter)
                    number_of_letters += 1

    # получаем ссылку на вторую страницу
    if page == 1:
        y = 0
        url = []
        for a in soup.find_all("a", class_='nBDE1b G5eFlf', limit=2):
            urls = a.get('href')
            urls = split_url + urls
            url.append(urls)
        # берем из двух ссылок вторую
        for url2 in url:
            if y == 1:
                url = url2
            y = + 1

    # получаем ссылку на 1 и 3-10 страницу
    else:
        for a in soup.find_all("a", class_='nBDE1b G5eFlf', limit=1):
            url = a.get('href')
            url = split_url + url
            page = +1
# удаляем лишнюю ссылку, которая почему-то каждый раз выводится по два раза
links.remove('https://www.youtube.com/watch%3Fv%3DbaPSUuyrBlI')
# выводим массив
print(links)
