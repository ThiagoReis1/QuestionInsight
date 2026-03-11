from numpy import * 

nt = array(eval(input("Notas: ")))

i = 0


while(i < size(nt)):
	if(nt[i] > 8):
		nt[i] = 10
	if(nt[i] < 2):
		nt[i] = 0
	i = i + 1
print(nt)