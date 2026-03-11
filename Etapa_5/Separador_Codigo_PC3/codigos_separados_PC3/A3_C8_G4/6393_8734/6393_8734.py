from numpy import*

vetor = array(eval(input('asd')))
lst = []

for num in vetor:
	num = int(num)
	x = (num + 1) ** 3  #numero que vai ser antecedido
	if num >= 9: #se ele for maior ou igual a 9 , vai dar 0
		x = 0
	lst.append(x)
print(array(lst))

