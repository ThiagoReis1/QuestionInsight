from numpy import*
temp = array(eval(input("digite: ")))
per = array(eval(input("digite: ")))
tam = size(temp)
cont = 0
soma = 0
while cont<tam :
	l = 5* per[cont]/100
	
	lit = l*temp[cont]
	soma = soma + lit
	cont = cont + 1
print(round(soma, 2))
	

