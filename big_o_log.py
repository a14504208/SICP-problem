def mul(a, b):
	remain = 0
	while True:
		if b == 1:
			return a + remain
		elif b == 0:
			return 0
		elif b % 2 == 0:
			a, b = a * 2, b // 2
		else:
			remain += a
			a, b = a, b - 1
			
def expo(x, n):
	remain = 1
	while True:
		if n == 0:
			return 1
		elif n == 1:
			return remain * x
		elif n % 2 == 0:
			x, n = x * x, n // 2
		else:
			remain *= x
			n = n - 1

def transform_n_times(a, b, p, q, n):
	while True:
		if n == 0:
			return b
		elif n % 2 == 0:
			n = n // 2
			p, q = transform_square(p, q)
		else:
			n -= 1
			a, b = b * q + a * (p + q), b * p + a * q

def transform_square(p, q):
	return p * p + q * q, 2 * p * q + q * q

def fib(n):
	return transform_n_times(1, 0, 0, 1, n)
