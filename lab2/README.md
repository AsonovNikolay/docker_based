# Без ⭐ (но ✨)

# Как работает

##### Запустить поды 

`kubectl apply -f web_app/deployment.yaml`

`kubectl apply -f web_app/service.yaml`  

`kubectl port-forward service/product-service 8081:80` 


> **Deployment используем для управления подами**

> **Service используем для сетевых настроек приложения**

*(3 пода по приколу сделаны, смысловой нагрузки нет)*  
 

Файлы можно, конечно, объеденить и запускать одной командой, но в целом не критично  

#### Проверить работоспособность  
`curl 127.0.0.1:8081`



--------

RAW(R) edit by Nicko

В Deployment описано создание 3 реплик techdozo/product-svc:1.0.0 (случайно взятый образ из docker hub, который поднимает RESTful приложение)  
https://hub.docker.com/r/techdozo/product-svc/tags  
Для того, чтобы получить доступ до приложения на локалхосте, прокидываем 8080 контейнера на 80 порт локалхоста в файле service.yaml
Именем продукта везде указно product, по имени образа

-----
Небольшая документация на приложение 
-----
The source code contains a microservice application, written in spring boot. This application exposes two end-points
1. `POST /products/`
2. `GET /products/{productId}`

To access end-points use curl

To save Product 
`curl --location --request POST 'localhost:81/products/' \
--header 'Content-Type: application/json' \
--header 'userId: abc@xyz.com' \
--data-raw '{
"name": "Apple iPhone 12",
"description": "Apple iPhone 12 Pro Max 128 GB, Pacific Blue",
"price": 1700
}'`

To get Product

`curl --location --request GET 'localhost:81/products/f02172fc-4bd6-44e1-869e-3bf3d0e35bd8' \
--data-raw ''`
