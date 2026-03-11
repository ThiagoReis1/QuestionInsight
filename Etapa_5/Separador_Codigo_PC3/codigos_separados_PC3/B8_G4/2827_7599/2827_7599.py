from numpy import *
nota = array(eval(input("notas:")))
i = 0
while(i<size(nota)):
	if(4<nota[i]<5):
		nota[i] = 4
	elif(9<nota[i]<10):
		nota[i] = 10
	i = i + 1
print(nota)