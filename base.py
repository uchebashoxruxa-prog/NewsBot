import requests
from bs4 import BeautifulSoup
from datetime import date
import sqlite3


def all_news(category):
    data = requests.get(f'https://kun.uz/en/news/category/{category}').text
    soup = BeautifulSoup(data, 'html.parser')
    news_block = soup.find('div', class_='news-page__list')
    blocks = news_block.find_all('a', class_='news-page__item l-item')
    host = 'https://kun.uz'
    today = date.today()
    list_news = []

    for block in blocks:
        title = block.find('h3').get_text(strip=True)
        link = host + block.get('href')
        date_time = block.find('p').get_text()

        if '/' not in date_time:
            date_time += f' / {today.strftime("%d.%m.%Y")}'

        list_news.append(f'Title: {title}\n\nReleased: {date_time}\n\n👉: {link}')

    return list_news


def create_table_users():
    db = sqlite3.connect('news.db')
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id BIGINT UNIQUE,
        username VARCHAR(100),
        phone VARCHAR(20),
        date DATE DEFAULT CURRENT_DATE
    )
    ''')
    db.commit()
    db.close()


def get_user(chat_id):
    db = sqlite3.connect('news.db')
    cursor = db.cursor()
    cursor.execute(f'''
    SELECT chat_id FROM users WHERE chat_id = ?
    ''', (chat_id,))
    user = cursor.fetchone()
    db.close()

    return user


def save_user_data(*args):
    db = sqlite3.connect('news.db')
    cursor = db.cursor()
    cursor.execute('''
    INSERT INTO users(chat_id, username, phone)
    VALUES (?, ?, ?)
    ''', args)
    db.commit()
    db.close()


# create_table_users()
