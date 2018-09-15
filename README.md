Для запуска сервера нужно выполнить команду:

python3 server.py

Затем ввести в  URL браузера:

http://localhost:8000

Для запуска теста нужно выполнить команду:

python3 test.py

Сборка докера:

sudo docker build .

Запуск сервера в докере:

sudo docker run -p 8000:8000

После запуска вводим в браузер:

 http://localhost:8000


