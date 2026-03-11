import numpy as np

saq = eval(input())

qtd = 0
ind = []
count = 0

while( count < len(saq)):
		if(saq[count]<= 50):
			ind.append(count)
			qtd = qtd + 1
		count = count + 1

ind = np.array(ind,dtype = np.int)

print(qtd)
print(ind)