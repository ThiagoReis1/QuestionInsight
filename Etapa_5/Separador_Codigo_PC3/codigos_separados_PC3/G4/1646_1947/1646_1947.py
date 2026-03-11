from numpy import*
vetor=array(eval(input("Vetor de valores:")))
y = 0
for i in range(size(vetor)):
	if vetor[i] <= 50:
		y = y + 1
print(y)
x = zeros(y, dtype = int)
i = 0
for h in range(size(vetor)):
	if vetor[h] <= 50:
		x[i] = h
		i = i + 1
print(x)
	