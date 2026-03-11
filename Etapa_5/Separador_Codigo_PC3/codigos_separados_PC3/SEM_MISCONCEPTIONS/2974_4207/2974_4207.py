qntd= int(input("DIGITE A QUANTIDADE DE ACAI NO COPO: "))
qntds= int(input("DIGITE A QUANTIDADE DE SALGADO: "))
valor= float(input("DIGITE O VALOR PAGO EM DINHEIRO: "))

totalsalg= qntds*3
totalacai= (qntd/1000)*24
total= totalsalg + totalacai

if(total<valor):
	print(round(total, 2))
	print("Sim")
else: 
	print(round(total, 2))
	print("Nao")
