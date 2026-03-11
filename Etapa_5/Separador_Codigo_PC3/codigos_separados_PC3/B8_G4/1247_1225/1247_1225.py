from numpy import*
# Leitura do primeiro vetor
x = array(eval(input("Primeiro vetor: ")))
A=min(x)
B=max(x)
C = 0.75 * A + 0.25 * B
D = 0.25 * A + 0.75 * B
cont = zeros (2,dtype = (int))
for i in (range(size (x))):
	if x[i]>= A and x[i] <C:
		cont[0]=cont[0] + 1
	elif(x[i] >= D) and (x[i] < B):
		cont[1]=cont[1] + 1
print(cont)