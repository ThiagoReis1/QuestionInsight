comida= input('L ou P: ')
a= int(input())
b= int(input(''))

if(comida=="L"):
	calculo=a*6+b*3
else:
	calculo=a*4.50+b*3
print(round(calculo,2))