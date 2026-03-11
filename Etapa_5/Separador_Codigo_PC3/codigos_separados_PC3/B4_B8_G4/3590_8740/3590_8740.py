from numpy import*
x = array(eval(input("aneis")))
p = 0
cont = 0
while p<size(x):
	if x[p] == 1:
		cont = cont + 10
	elif x[p] == 2:
		cont = cont + 5
	elif x[p] == 3:
		cont = cont + 0
	elif x[p] == 4:
		cont = cont + 5
	elif x[p] == 5:
		cont = cont + 20
	elif x[p] == 6:
		cont = cont + 10
	p = p + 1
print (cont)