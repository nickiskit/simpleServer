Для запуска сервера нужно выполнить команду:

python3 server.py

Затем ввести в  URL браузера:

http://localhost:9000

Для запуска теста нужно выполнить команду:

python3 test.py

Сборка докера:

sudo docker build -t docker_name .

Запуск сервера в докере:

sudo docker run --rm -it  -p 9000:9000 docker_name

После запуска вводим в браузер:

 http://localhost:9000


