def isPrime(n):
	if n < 2:
		return False
	return sum(d for d in xrange(2, n) if n % d == 0) == 0
	
assert isPrime(1) == False # by definition
assert isPrime(2) == True
assert isPrime(3) == True
assert isPrime(4) == False
assert isPrime(13) == True
assert isPrime(23) == True
assert isPrime(30011) == True
assert isPrime(1009) == True
assert isPrime(17 * 19) == False
assert isPrime(16) == False
assert isPrime(101)
