Создать Image
docker build -t ip_get:1.0 . 

docker-compose up -d 
Поднять контейнер  (-d чтобы запстился в бэграунд)

docker logs bot_app -f
Посмотреть логи контейнера 