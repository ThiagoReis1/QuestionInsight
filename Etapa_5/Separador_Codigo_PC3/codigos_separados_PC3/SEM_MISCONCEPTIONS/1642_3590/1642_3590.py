entrada = eval(input())
total = 0
saida = []

for i in range(len(entrada)):
	if(entrada[i] % 5 == 0 and entrada[i] != 0):
		total += 1
		saida.append(i)


print(total)
print('[',end='')
for i in range(len(saida)):
	if(i == len(saida) -1):
		print(saida[i],end=']')
	else:
		print(saida[i],end=' ')

if(total == 0):
	print(']')