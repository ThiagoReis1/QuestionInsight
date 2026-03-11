from numpy import*
saques = array(eval(input("Insira os saques: ")))

num = 0
for i in range(size(saques)):
	if(saques[i] <= 50):
		num += 1
print(num)

saida = zeros(num, dtype=int)
a = 0
b = 0
for i in range(size(saques)):
	if(saques[i]<50):
		a += 1
	elif(saques[i]<=50):
		saida[b] = saida[b] + a
		a += 1
		b += 1
print(saida)
