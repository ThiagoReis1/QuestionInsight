g= int(input("Pontos de Força dos Guerreiros: "))
t= int(input("Pontos de Força Inicial do Troll: "))
t1= int(input("Pontos de Força Recuperada do Troll: "))

x = 0
b = 0

while  0<b:
	b = t - g*5 + t1
	x+=1
	print(x)