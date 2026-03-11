from numpy import *

uf = ['AZ','CA', 'FL', 'PA', 'WI']

entrada = input().split(',')

total = 0
qtd_uf = [0,0,0,0,0]

for i in range(len(entrada)):
	for n in range(5):
		if entrada[i].upper() == uf[n]:
			qtd_uf[n] += 1
	
total = max(qtd_uf)

print(total)
print(array(qtd_uf))
	