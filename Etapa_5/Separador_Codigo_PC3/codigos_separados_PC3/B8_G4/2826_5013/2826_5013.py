from numpy import*
n = array(eval(input("Digite o vetor: "))) #vetor de notas


i = 0
while(i < size(n)):
	if(n[i] > 8):
		n[i] = 10
	elif(n[i] < 2):
		n[i] = 0
	elif(n[i] < 8 and n[i] > 2):
		n[i] = n[i]
	i = i + 1
	
print(n)
