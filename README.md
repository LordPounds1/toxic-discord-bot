# 🤖 Toxic Discord Bot / Токсичный Discord-бот

Проект по автоматическому определению токсичных комментариев с помощью модели машинного обучения.  
Бот интегрирован с Discord и способен реагировать на оскорбительные сообщения.

A machine learning project for detecting toxic comments with a Discord bot integration.  
The bot reacts to offensive messages and gives feedback instantly.

---

## 📌 Описание / Description

🔷 **Русский**  
Модель обучена с использованием TF-IDF и Logistic Regression, F1 ≥ 0.75.  
Поддерживается Flask API и Discord-бот, реагирующий на токсичные сообщения.

🔷 **English**  
Model trained using TF-IDF and Logistic Regression (F1 ≥ 0.75).  
Includes a Flask API and Discord bot that responds to toxic messages.

---

## 📂 Структура проекта / Project Structure

| Файл / Папка         | Назначение / Purpose                      |
|----------------------|-------------------------------------------|
| `bot.py`             | Discord-бот / Discord bot                 |
| `server.py`          | Flask API                                 |
| `requirements.txt`   | Зависимости / Python dependencies         |
| `Dockerfile`         | Docker-сборка API                         |
| `.env.example`       | Пример переменных окружения / Env example|

---

## 🚀 Быстрый старт / Quick Start

### 🐍 Установка зависимостей / Install dependencies

```bash
pip install -r requirements.txt
```
### 🔬 Запуск API / Run Flask API

```bash
python server.py
```

### 🤖 Запуск Discord-бота / Run Discord bot

Создай .env:
```bash
DISCORD_TOKEN=твой_токен_бота / your_discord_token
```

Запуск:
```bash
python bot.py
```

## 🐳 Docker
Сборка и запуск API:

```bash
docker build -t toxic-api .
docker run -d -p 8081:8081 --name toxic toxic-api
```

## 📡 Пример API запроса / Example API Request
![Пример токсичного ответа](https://i.imgur.com/jGiS5Va.png)
![Пример не токсичного ответа](https://i.imgur.com/oOS4wzA.png)

## 👨‍💻 Автор / Author
GitHub: LordPounds1
Telegram: [https://t.me/Tsp312]
