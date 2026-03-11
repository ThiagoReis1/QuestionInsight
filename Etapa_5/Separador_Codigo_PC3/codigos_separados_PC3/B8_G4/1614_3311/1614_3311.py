from numpy import*
nome = array(eval(input("Digite:")))
qtd = array(eval(input("Digite:")))
cont = 0
soma = 0
while(cont<size(qtd)):
	if(nome[cont].upper()=="BANANA"):
		soma = soma + 0.97*qtd[cont]
	elif(nome[cont].upper()=="BIFE"):
		soma = soma + 2.95*qtd[cont]
	elif(nome[cont].upper()=="FEIJOADA"):
		soma = soma + 1.27*qtd[cont]
	elif(nome[cont].upper()=="OMELETE"):
		soma = soma + 1.04*qtd[cont]
	elif(nome[cont].upper()=="TOMATE"):
		soma = soma + 0.2*qtd[cont]
	cont=cont+1
print(round(soma,2))