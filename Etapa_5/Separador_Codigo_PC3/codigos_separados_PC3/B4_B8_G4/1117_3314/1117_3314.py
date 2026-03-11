from math import *
x=float(input("Digite o preco da entrada: "))
y=int(input("Digite o dia da semana: "))
z=input("Eh dia de musica ao vivo: ").upper()
print("Entradas: ", x, "," , y,"," , z)
if (y >= 1) and (y < 7):
	if z == "S":
		if (y==1):
			d=x+20
			print("Valor a pagar: R$",round(d,2))
		elif (y==2):
			d= x-(x*0.25)
			t= d+20
			print("Valor a pagar: R$",round(t,2))
		elif (y==3):
			d= x-(x*0.25)
			t= d+20
			print("Valor a pagar: R$",round(t,2))
		elif (y==4):
			d= x+20
			print("Valor a pagar: R$",round(d,2))
		elif (y==5):
			d= x-(x*0.25)
			t= d+20
			print("Valor a pagar: R$",round(t,2))
		elif (y==6):
			d= x+20
			print("Valor a pagar: R$",round(d,2))
		elif (y==7):
			d= x+20
			print("Valor a pagar: R$",round(d,2))	
	else:
		if (y==1):
			print("Valor a pagar: R$",round(x,2))
		elif (y ==2):
			d= x-(x*0.25)
			print("Valor a pagar: R$",round(d,2))
		elif (y==3):
			d= x-(x*0.25)
			print("Valor a pagar: R$",round(d,2))
		elif (y==4):
			print("Valor a pagar: R$",round(x,2))
		elif (y==5):
			d= x-(x*0.25)
			print("Valor a pagar: R$",round(x,2))
		elif (y==6):
			print("Valor a pagar: R$",round(x,2))
		elif (y==7):
			print("Valor a pagar: R$",round(x,2))
else:
	print("Dados invalidos")
	
