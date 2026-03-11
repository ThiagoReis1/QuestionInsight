from numpy import*
n = array(eval(input("notas: ")))
soma = 0

for i in range(size(n)):
	soma = soma + n
	m = soma/size(n)
	if m < 5:
		cont = cont +1
		print(cont)
			 
