# faça seu código aqui!

A = 28.5 
Horario_Compra = float(input("Qual foi o horaio de compra ?"))
Quantidade = float(input("Quantos pratos foram comprados ?"))
conta = A*Quantidade

if Horario_Compra >= 18:
	print (round(conta*0.8,2))
else:
	print(round(conta,2))