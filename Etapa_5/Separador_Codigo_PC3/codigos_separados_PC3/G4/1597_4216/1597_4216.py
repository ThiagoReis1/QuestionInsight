from numpy import*
n = array(eval(input("insira os valores: ")))
soma = sum(n)
desconto = (5/100)*soma
i = 0 

while(i<size(n)):
	if(n[i]>=80):
		soma =  soma - desconto
	i = i + 1

print(round(soma, 2))



		
	