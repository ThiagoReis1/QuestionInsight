#Thaynara Marques
#ap5
from numpy import*
rio2016= array(eval(input("Digite lançamentos da Rio2016:")))
recorde = 74.08
i = 0
numlan = 0
while (i<size(rio2016)):
	if (rio2016[i]<recorde):
		numlan = numlan +1
	i = i+1
print(recorde)
print(numlan)