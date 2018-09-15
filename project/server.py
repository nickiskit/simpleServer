import socket

URLS = {
				'/': 'index',
				'/fac': 'factorization'
}

def factorization(number):
#Функция факторизующая число
	i = 2
	list_prime_numbers = []
	while i**2 <= number:
		while number % i == 0:
			list_prime_numbers.append(i)
			number = number / i
		i += 1
	if number > 1:
		list_prime_numbers.append(int(number))
	prime_numbers = ' '.join(map(str, list_prime_numbers))
	return prime_numbers

def parse_data(data):
#Обработка запроса клиента
	if data == '':
		method = 'GET'
		url = '/'
	else: 
		parsed = data.split(' ')
		method = parsed[0]
		url = parsed[1]
	return (method, url)

def generate_headers(method, url):
#Функция, формирующая хедеры
	if method != 'GET':
		return ('HTTP/1.1 405 method not found\n\n', 405)
	if  url not in URLS:
		return ('HTTP/1.1 404 ERROR\n\n', 404)
	return ('HTTP/1.1 200 OK\n\n', 200)


def generate_html_page(code, url, number):
#Фцнкция, формирующая html-страницу
	if code == 404:
		return '<h1>404</h1><p>ERROR</p>'
	if code == 405:
		return '<h1>405</h1><p>Method not found</p>' 
	if url == '/': 
		return '<h1>Enter number</h1><link rel="icon" href="data:,"><div><form method="GET" action="/fac"><input type="text" name="number" value="" /><button>Enter</button></form></div>'
	if url == '/fac':
		try:
			if float(number) <= 1:
				return '<h1>This number can not be factorized</h1>'
			return factorization(int(number))
		except:
			return '<h1>This is not number</h1>'
		

def server_response(data):
#Функция, формирующая ответ клиенту от сервера
	method, url = parse_data(data)
	if url != '/':
		try:
			number = (url.split('='))[1]
			url = url.split('?')[0]
		except:
			number = '0' 
	else:
		number = '0' 
	headers, code = generate_headers(method, url)
	html_page = generate_html_page(code, url, number)
	return (headers + html_page).encode()


def server():
#Создание сервера
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind(('0.0.0.0', 9000))
	sock.listen()
	while True:
		conn, addr = sock.accept()
		data = conn.recv(1024)
		print('connected:', addr)
		response = server_response(data.decode('utf-8'))
		conn.sendall(response)
		conn.close()


if __name__ == '__main__':
	server()