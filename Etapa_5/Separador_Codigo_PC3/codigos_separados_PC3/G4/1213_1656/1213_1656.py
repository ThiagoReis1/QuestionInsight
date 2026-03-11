from numpy import*
v = array(eval(input("Digite os pesos levantados pelos atletas: ")))
i = 0
k = 0
recorde = 217
while(i < size(v)):
	if(v[i] > recorde):
		k = k + 1
	i = i + 1
print(recorde)
print(k)