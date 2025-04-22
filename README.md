# 🤖 Toxic Discord Bot / Токсичный Discord-бот

Проект по автоматическому определению токсичных комментариев с помощью модели машинного обучения.
Бот интегрирован с Discord и способен реагировать на оскорбительные сообщения на русском и английском языках.

A machine learning project for detecting toxic comments with Discord bot integration.
The bot responds to offensive messages in both Russian and English.

---

## 📌 Описание / Description

🔷 Русский
Модель обучена с использованием TF-IDF и Logistic Regression

F1-score ≥ 0.79

Реализованы:

REST API на Flask

Discord-бот, реагирующий на токсичные сообщения

Поддержка двух языков (английский и русский)

Автозапуск через systemd

🔷 English
Model trained using TF-IDF and Logistic Regression

F1-score ≥ 0.79

Includes:

Flask-based REST API

Discord bot that reacts to toxic messages

Dual language support (EN + RU)

Auto-start via systemd service

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
![An example of a toxic response](https://i.imgur.com/xQ4EDAp.png)
![An example of a non-toxic response](https://i.imgur.com/GKR48Yf.png)
![Пример нетоксичного ответа](https://i.imgur.com/IxonfPJ.png)
![Пример токсичного ответа](https://i.imgur.com/VyRGf9R.png)

## 👨‍💻 Автор / Author
GitHub: LordPounds1

Telegram: [https://t.me/Tsp312]
