n = int(input("Nº copiais iniciais:"))
tax = float(input("Taxa de redução:"))
cop = int(input("Cópias introduzidas por semana:"))

sem = 0
t = tax/100
x = 1000000

while(n <= x):
	n = n - (n * t)
	c = n + cop
	n = c
	sem = sem + 1
print(sem)