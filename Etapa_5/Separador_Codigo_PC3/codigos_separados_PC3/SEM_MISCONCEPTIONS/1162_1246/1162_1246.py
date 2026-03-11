#Karoline Oliveira da Costa
#av4 ex.1
#28 de julho de 2016
valor_recebido=float(input("Digite o valor recebido: "))
rendimento=float(input("Digite o rendimento: "))
valor_gasto=int(input("Digite o valor gasto: "))
#variavel acumuladora
valor=valor_recebido
#variavel contadora
m=1
while(valor>0):
	valor=(valor_recebido + (rendimento*valor_recebido)) - (valor_gasto)
	m=m+1
	print(valor)
