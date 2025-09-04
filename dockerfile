# Используем официальный образ Python
FROM python:3.11-slim

# Создаем рабочую директорию
WORKDIR /app

# Скопируем requirements.txt и установим зависимости
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Скопируем весь проект внутрь контейнера
COPY . .

# Запускаем бота
CMD ["python", "main.py"]
