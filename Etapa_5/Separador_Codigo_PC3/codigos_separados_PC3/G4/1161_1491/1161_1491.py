z = int(input("quantos zumbis invadiram? "))
h = int(input("habitantes da vila: "))
x = int(input("zumbi que transforma hab: "))
y = int(input("exterminadores de zumbi: "))

dia = 0
while(h > 0):
	z = z * x
	z = z - y
	h = h - z
	dia = dia + 1
print(dia)