qa=int(input('quantidade de acai no copo: '))
qs=int(input('quantidade de salgados: '))
valor=float(input('valor pago: '))
acai=24/qa 
salgado=qs*3
calculo=valor-(acai + salgado)

print(float(round(calculo, 2)))
if calculo>0:
	mensagem= 'sim'
else:
	mensagem= 'nao'
print(mensagem)