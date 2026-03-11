from numpy import*

k = array(eval(input("Abra: ")))
c = zeros(size(k), dtype=int)

for i in range(size(k)):
	if k[i] == 0:
		k[i] = 9**2
	else:
		k[i] = (k[i] - 1)**2
print(k)