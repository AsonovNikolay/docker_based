# Лабораторная работ №3 #

## Цель работы ##
Сделать автоматичкую сборку образа и настроить его сохранение на Dockerhub
## Ход работы ##
Первым делом необходимо сохранить перемнные окружнения, для того чтобы в будущем мы могли их использовать для автоматического входа в DockerHub.

![изображение](https://github.com/AsonovNikolay/docker_based/assets/71012423/db660980-1f3d-4d9e-a775-22e250b03e25)


Далее мы настроили файл docker-image.yml который находится по пути .github/workflows

```
name: Auto_push_docker_image

on:
  push: #сценарий должен запускать при пуше в ветку main
    branches: [ "main" ]
    paths:  #директории и файлы в которых должны появиться изменения
      - "lab3/bot/**"
      - ".github/workflows/docker-image.yml"

jobs:
  build_and_run:

    runs-on: ubuntu-22.04 #образ который используется для выполнения команд

    steps: #шаги для выполнения сценария
    - name: checkout_rep #для клонирования репозитория в рабочее пространство
      uses: actions/checkout@v4

    - name: Log_in_DockerHub #авторизация в систему DockerHub
      uses: docker/login-action@v3
      with:
        username: ${{ secrets.DOCKER_USERNAME }} #логин для авторизации в DockerHub
        password: ${{ secrets.DOCKER_PASSWORD }} #пароль для авторизации в DockerHub


    - name: Build_and_push_docker_image #сборка и пуш в DockerHub
      uses: docker/build-push-action@v5
      with:
        context: "./lab3" #расположение файла для сборки Docker-образа
        push: true
        tags: fiji6479/ip-get:1.0 #Название и версия образа на DockerHub
```
Рассмотрим подробнее код, который у нас получился

Укажем название сценария
```
name: Auto_push_docker_image
```

В этой части кода мы задаем параметры для сборки образа.
```
on:
  push: #сценарий должен запускать при пуше в ветку main
    branches: [ "main" ]
    paths:  #директории и файлы в которых должны появиться изменения
      - "lab3/bot/**"
      - ".github/workflows/docker-image.yml"
```
Указываем образ который используется для выполнения команд.

```
jobs:
  build_and_run:

    runs-on: ubuntu-22.04 #образ который используется для выполнения команд
```

Первым шагом для нашего сценария будет клонирование репозитория в рабочее пространство.
```
steps: #шаги для выполнения сценария
    - name: checkout_rep #для клонирования репозитория в рабочее пространство
      uses: actions/checkout@v4
```
Вторым шагом настроим автоматическую авторизацию в DockerHub. Здесь мы и будет использоыать перемнные DOCKER_USERNAME и DOCKER_PASSWORD, который мы заранее добавили.
```
    - name: Log_in_DockerHub #авторизация в систему DockerHub
      uses: docker/login-action@v3
      with:
        username: ${{ secrets.DOCKER_USERNAME }} #логин для авторизации в DockerHub
        password: ${{ secrets.DOCKER_PASSWORD }} #пароль для авторизации в DockerHub
```
И третьим шагом мы настроим сборку образа с помощью build-push-action@v5

```
  - name: Build_and_push_docker_image #сборка и пуш в DockerHub
      uses: docker/build-push-action@v5
      with:
        context: "./lab3" #расположение файла для сборки Docker-образа
        push: true
        tags: fiji6479/ip-get:1.0 #Название и версия образа на DockerHub
```
Проверим работоспособность yml файла.

![изображение](https://github.com/AsonovNikolay/docker_based/assets/71012423/0499747b-96a4-47b1-90fa-6f9cb2566c3d)

![изображение](https://github.com/AsonovNikolay/docker_based/assets/71012423/1d1b357a-2f5c-47ee-ac83-1e4823ec1504)


## Вывод ##

В ходе выполнения лабораторной работы мы настроили автоматичкую сборку и отправку образа на DockerHub после пушу в репозиторий. 
