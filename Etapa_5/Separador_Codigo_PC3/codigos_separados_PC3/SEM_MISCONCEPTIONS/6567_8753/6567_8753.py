# faça seu código aqui!
speed = float(input("velocidade: "))

if (speed < 50):
	valor = 60 + 4.5
	print("total=",round(valor, 2))
elif (speed == 50):
	valor = 60 + 5.5
	print("total=",round(valor, 2))
else :
	valor = 60 + 6.5
	print("total=",round(valor, 2))