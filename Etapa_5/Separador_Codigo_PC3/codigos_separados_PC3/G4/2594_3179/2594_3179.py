from numpy import*
d = array(eval(input("Digite o vetor das demandas: ")))
#d[0]--> quantidade critica
#ac >= d[0]
ac = 0

for i in range(size(d)):
	if(d[i] >= d[0] and d[i] != d[0]):
		ac = ac + 1
print(size(d[0]))
print(ac)	