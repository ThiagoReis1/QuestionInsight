# faça seu código aqui!

v = int(input("Insira a velocidade escolhida pelo cliente em Mbps: "))

if (v<50):
	valor = 60 + 4.5
elif (v==50):
	valor = 60 + 5.5
else:
	valor = 60 + 6.5
print("total=", round(valor, 2))