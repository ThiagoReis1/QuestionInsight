preferencia = input("(T/S): ")
qntde = int(input("Quantidade de tapioca(s) ou salgado(s): "))
acai = int(input("Quantidade de acai(s): "))

valor = qntde * 4.50
valor2 = qntde * 5
valor3 = acai * 12

if (preferencia.upper() == "T"):
	print(round(valor + valor3,2))
	
else :
	print(round(valor2 + valor3,2))