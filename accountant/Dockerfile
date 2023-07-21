# # Используем базовый образ Python 3.9.14-slim-bullseye
# FROM python:3.9.14-slim-bullseye

# # Устанавливаем необходимые зависимости
# RUN apt-get update && apt-get install -y \
#     libpq-dev

# # Устанавливаем зависимости Python
# COPY requirements.txt /app/
# WORKDIR /app
# RUN pip install --no-cache-dir -r requirements.txt

# # Копируем исходный код Django в контейнер
# COPY . /app/

# # Экспозим порт Django
# EXPOSE 8000

# # Запускаем Django сервер
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# Используем более легковесный базовый образ
FROM python:3.9.14-alpine

# Устанавливаем необходимые зависимости
RUN apk add --no-cache libpq

# Копируем файлы зависимостей Python и устанавливаем их
COPY requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код Django в контейнер
COPY . /app/

# Экспозим порт Django
EXPOSE 8000

# Запускаем Django сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

