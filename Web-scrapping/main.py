import requests
from bs4 import BeautifulSoup
from datetime import datetime

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

url = 'https://habr.com/ru/articles/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

# Находим все статьи на странице
articles = soup.find_all('article', class_='tm-articles-list__item')

# Проходим по каждой статье и проверяем наличие ключевых слов
for article in articles:
    title_element = article.find('h2', class_='tm-title')
    if not title_element:
        continue
    title = title_element.text.strip()

    # Получаем ссылку на статью
    link_element = title_element.find('a', class_='tm-title__link')
    if not link_element:
        continue
    link = 'https://habr.com' + link_element['href']

    # Получаем дату публикации статьи
    date_element = article.find('time')
    if not date_element:
        continue
    date_str = date_element['datetime']
    try:
        date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    except ValueError:
        continue

    # Получаем текст превью статьи
    preview_element = article.find('div', class_='tm-article-body')
    if not preview_element:
        continue
    preview = preview_element.text.strip()

    # Проверяем, содержит ли превью хотя бы одно из ключевых слов
    if any(keyword.lower() in preview.lower() for keyword in KEYWORDS):
        print(f'{date.strftime("%Y-%m-%d")} – {title} – {link}')