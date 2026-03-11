z = int(input("Quantos zumbis invadiram?"))
h = int(input("Quantos habitantes existem na vila?"))
x = int(input("Kda zumbi transfoma quantas people?"))
y = int(input("Quantos The Wallking Dead matam por dia?"))
day = 0
while(h > 0):
	z = z * x
	z = z - y
	h = h - z
	day = day + 1
print(day)