from numpy import*
num = array(eval(input("Numeros: ")))
n = zeros(size(num),dtype=int)

for i in range(size(num)):
	if num [i] == 9:
		n[i] == 0
	else:
		n[i] = (num[i]+1)** 3
print(n)