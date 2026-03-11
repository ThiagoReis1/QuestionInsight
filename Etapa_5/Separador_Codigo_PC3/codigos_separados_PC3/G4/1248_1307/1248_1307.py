from numpy import*
x = array(eval(input("Digite um vetor: ")))

A = min(x)
B = max(x)
C = 0.75 * A + 0.25 * B
D = 0.25 * A + 0.75 * B

j = 0
k = 0
for i in x:
	if(i >= C and i < D):
		j = j + 1
	if(i >= D and i < B):
		k = k + 1
z = array([j,k])
print(z)