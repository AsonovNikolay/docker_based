FROM python:3.8

WORKDIR /tg_bot_ip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Копируйте все файлы проекта в контейнер
COPY . /tg_bot_ip

#ARG OC=my_default_value

# Определите команду для запуска вашего бота
#CMD ["python", "./bot/IPbot.py", "OC"]
CMD ["python", "/tg_bot_ip/bot/IPbot.py"]
