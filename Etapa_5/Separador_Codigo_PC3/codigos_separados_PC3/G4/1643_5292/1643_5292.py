from numpy import*

notas = array(eval(input("insira as notas dos alunos:  ")))
cont = 0
a = 5.0
for i in range(size(notas)):
	if notas[i] >= a:
		cont += 1
print(cont)

apro = zeros(cont, dtype = int)
j = 0
for i in range(size(notas)):
	if notas[i] >= a:
		apro[j] = i
		j += 1
print(apro)
		