from numpy import*

qtd = 0
e = array(eval(input("Digite os nomes dos estados: ")))

for i in range(size(e)):
	if(e[i] == 'AZ'):
		qtd = qtd + 1
	elif(e[i] == 'CA'):
		qtd = qtd + 1
	elif(e[i] == 'FL'):
		qtd = qtd + 1
	elif(e[i] =='PA'):
		qtd = qtd + 1
	else
		