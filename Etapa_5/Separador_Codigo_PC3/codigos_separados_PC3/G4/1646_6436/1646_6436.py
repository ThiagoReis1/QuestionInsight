from numpy import*
x = array(eval(input("")))

cont = 0

for i in range(size(x)):
	if x[i] <= 50:
		cont += 1
print(cont)
result = zeros(cont, dtype = int)
j = 0
for i in range(size(x)):
	if x[i] <= 50:
		result[j] = i
		j += 1
print(result)