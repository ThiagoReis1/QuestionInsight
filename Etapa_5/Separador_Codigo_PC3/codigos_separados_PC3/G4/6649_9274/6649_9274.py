from numpy import *
peso = [3,2,4,1,3]
notasaluno = array(eval(input("notas")))
i = 0
n=0
while i<size(notasaluno):
	n = n + notasaluno[i]*peso[i]
	i = i + 1
print(round(n/sum(peso),2))
