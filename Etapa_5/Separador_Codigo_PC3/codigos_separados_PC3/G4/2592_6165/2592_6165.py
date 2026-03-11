from numpy import*

ubs = array(eval(input("")))

i = 1
qnt = 0

while(i < size(ubs)):
	if(ubs[i] >= ubs[0]):
		qnt = qnt + 1
		print(i)
	i = i + 1
print(qnt)