from numpy import*

v = array(eval(input("Vetor de alunos:")))

par = 0
impar = 0


for i in range(size(v)):
	if (v[i] % 2 == 0):
		par = par + 1
	else:
		impar = impar + 1
		print(impar)

for j in range(size(impar)):
	impar[i] = j
	print(v[i])