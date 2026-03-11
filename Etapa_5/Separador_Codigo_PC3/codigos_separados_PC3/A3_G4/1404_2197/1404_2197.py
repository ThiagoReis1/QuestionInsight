nome_da_cabeca = input("Digite o nome da cabeça que irá atacar: ")
var1 = int(input("Digite valor de var1: "))
var2 = int(input("Digite valor de var2: "))
var3 = int(input("Digite valor de var3: "))

s = ((var1/10)+(var2/10)+(var3/10))*10
m = (2 * ((var1/10)+ (var2/10) + (var3/10)))*10

if m < s:
	perda_de_vida = s
	print(round(perda_de_vida, 2))
else:
	perda_de_vida = m
	print(round(perda_de_vida, 2))