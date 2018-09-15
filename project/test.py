import unittest
import server

class server_test(unittest.TestCase):
	def test_factorization(self):
		self.assertEqual(server.factorization(123), '3 41')
    
	def test_factorization(self):
		self.assertEqual(server.factorization(17), '17')

	def test_headers(self):
		self.assertEqual(server.generate_headers('GET', '/asdf'), ('HTTP/1.1 404 ERROR\n\n', 404))

	def test_headers(self):
		self.assertEqual(server.generate_headers('POST', '/'), ('HTTP/1.1 405 method not found\n\n', 405))

	def test_content(self):
		self.assertEqual(server.generate_html_page(202, '/fac', '-23'), '<h1>This number can not be factorized</h1>')

	def test_content(self):
		self.assertEqual(server.generate_html_page(202, '/fac', '0.5'), '<h1>This number can not be factorized</h1>')

	def test_content(self):
		self.assertEqual(server.generate_html_page(202, '/fac', 'number'), '<h1>This is not number</h1>')


if __name__ == '__main__':
    unittest.main()