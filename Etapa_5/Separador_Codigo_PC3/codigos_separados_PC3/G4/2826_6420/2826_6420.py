from numpy import*

n = array(eval(input("Vetor de notas:")))

i = 0

while(i < size(n)):
	if (n[i] > 8):
		n[i] = 10
	if (n[i] < 2):
		n[i] = 0
	i = i + 1 
print(n)
	
		