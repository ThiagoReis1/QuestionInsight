from numpy import*

p = array(eval(input()))
a = array(eval(input()))

imc = p/(a**2)

i=0


while (i<size(imc)):
	for x in imc:
		if(imc[i]<17):
			situacao = "MUITO ABAIXO DO PESO"
		elif(imc[i]>=17 and imc[i]<= 18.49):
			situacao = "ABAIXO DO PESO"
		elif(imc[i]>=18.5 and imc[i]<=24.99):
			situacao = "PESO NORMAL"
		elif(imc[i]>=25 and imc[i]<=29.99):
			situacao = "ACIMA DO PESO"
		elif(imc[i]>=30 and imc[i]<=34.99):
			situacao = "OBESIDADE"
		elif(imc[i]>=35 and imc[i]<=39.99):
			situacao = "OBESIDADE SEVERA"
		else:
			situacao = "OBESIDADE MORBIDA"
	i=i+1

	
print(imc)
print("O MAIOR IMC DA TURMA EH:", round(max(imc),2), situacao)