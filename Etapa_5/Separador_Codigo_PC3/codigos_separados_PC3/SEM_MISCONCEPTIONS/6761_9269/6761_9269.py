velocidade = int(input("digite a velocidade da internet: "))
assinatura = 60

if (velocidade < 50):
	total = assinatura + 4.50 
elif (velocidade == 50):
	total = assinatura + 5.50
else:
	total = assinatura + 6.50
print(total)