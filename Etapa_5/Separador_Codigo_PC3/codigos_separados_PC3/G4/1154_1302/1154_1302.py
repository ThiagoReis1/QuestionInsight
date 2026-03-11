n = int(input("numero de copias/ml: "))
t = float(input("taxa de reducao: "))
i = int(input("numero e copias introduzidas/semana: "))
s = numero_de_semanas

while (n <= 1000000):
	print(s)
	s = n + t * n - n/(i)


