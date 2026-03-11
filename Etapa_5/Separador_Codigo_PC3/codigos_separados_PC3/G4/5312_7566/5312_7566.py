x = int(input("insira o numero de bacterias: "))
h = int(input("insira quantidade de horas: "))
e = 0
a = x
while(e!=h):
	a = a + int(a*0.02)
	e = e + 1

print(a)
	