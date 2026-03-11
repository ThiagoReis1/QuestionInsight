x = float(input(""))
k = int(input(""))

contador = 0 
angulo = 0
exp= 1
while( contador != k):
	angulo = angulo + (x ** exp)/exp
	exp = exp + 2
	contador = contador + 1
print(round(angulo,7))