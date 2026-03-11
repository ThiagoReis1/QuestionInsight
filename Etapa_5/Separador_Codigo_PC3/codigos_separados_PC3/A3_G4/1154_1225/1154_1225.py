n = int(input("Copias iniciais: "))
t = float(input("Taxa percentual: "))
n2 = int(input("Copias por semana: "))
cs = 0
s = 0
semanas = (n+t/100+n2)
while (semanas<=1):
	print("estado critico")