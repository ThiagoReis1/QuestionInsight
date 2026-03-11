import numpy as np

list = np.array(eval(input()))
pesos = [3,4,2,1,4,5]
sum_total = 0

for i in range(0,6):
	sum_total += int(list[i]) * int(pesos[i])


print(round(sum_total/sum(pesos),2))