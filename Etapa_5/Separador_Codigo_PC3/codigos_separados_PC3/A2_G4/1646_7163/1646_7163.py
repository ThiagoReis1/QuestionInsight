from numpy import*
#
v = array(eval(input("insira  os valores: ")))
# variavel contadora
j = 0
#laço 1
for i in range(size(v)):
	if v[i] <= 50:
		j = j + 1
	else:
		j = j
print(j)
#vetor nulo
nul = zeros(j,dtype = int)
#variavel contadora
k = 0
#laço 2
for i in range(size(v)):
	if v[i] <= 50:
		nul[k] = i
		k = k + 1
print(nul)