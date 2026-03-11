from numpy import *
ci = array(eval(input("valores dos itens:")))
i = 0
nci = zeros(size(ci))
while(i < size(ci)):
	if(ci[i] > 80):
		nci[i] = ci[i] - 5
		i = i + 1
	else:
		nci[i] = ci[i]
		i = i + 1
print(round(sum(nci),2))		