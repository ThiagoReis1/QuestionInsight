n = int(input(""))
a = n//100           #2primeirosnumeros
b = (n//10)%10       #
c = n % 10           #
d = (b*10) + c       #2ultimosnumeros
m = (a + d)**2
if(n == m):
	r = ("atende")
else:
	r = ("nao atende")
print(n)
print(r)