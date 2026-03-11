# faça seu código aqui!
qd = int(input("quantos dias deseja ter a posse do carro: "))

valor = qd * 100.00

if(qd<7):
	total= valor + 15.00
	print(round(total,2))
elif(qd==7):
	total= valor + 12.00
	print(round(total,2))
else:
	total= valor + 10.00
	print(round(total,2))