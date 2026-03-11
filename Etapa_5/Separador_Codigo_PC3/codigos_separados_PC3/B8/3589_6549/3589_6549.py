from numpy import*

aneis = array(eval(input("")))

cont = 0
soma = 0

while(cont < size(aneis)):
	if(aneis[cont] == 1):
		soma += 80
	elif(aneis[cont] == 2):
		soma += 40
	elif(aneis[cont] == 3):
		soma += 20
	elif(aneis[cont] == 4):
		soma+= 10
		
	cont +=1
print(soma)
	