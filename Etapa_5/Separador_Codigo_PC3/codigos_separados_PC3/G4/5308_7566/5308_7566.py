x = float(input("insira um numero: "))
k = int(input("insira a quantidade de termos: "))
e = 1
a = 0
while(e<=k):
	s = e/(2*e*x)
	a = a + s
	e = e + 1

print(round(a, 10))