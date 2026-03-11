horas = float(input("digite um numero: "))
#salario com 20 horas ou menos de aula:
salario = horas * 50
#horas a mais de aula:
qh = horas-20
#pagamento por horas extras de aula:
pagamento = ((50*20)+(70*qh))
if  (horas <= 20):
	  mensagem = salario
else:
	  mensagem = pagamento
print(round(mensagem,2))

    