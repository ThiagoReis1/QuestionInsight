comida = input('T ou S: ')
a = int(input())
b = int(input(''))

if (comida=="T"):
	calculo= a*5.50+b*10
else:
	calculo=a*4 + b*10
print(round(calculo,2))