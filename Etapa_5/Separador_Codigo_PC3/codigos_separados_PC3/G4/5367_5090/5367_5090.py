from numpy import*

cpf = array(eval(input("digitos: ")))

v = [1,2,3,4,5,6,7,8,9]
var =0
i = 0

while(i<size(cpf)):
	var = var +(cpf[i]*v[i])
	div = var%11
	i = i +1
print(div)