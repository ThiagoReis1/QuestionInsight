from numpy import*

vetor = array(eval(input("mensagem:" )))
lst = []

for num in vetor:
	num= int(num)
	x = (num +1)**3
	if num > 9:
		x=0
	lst.append(x)
print(array(lst))
