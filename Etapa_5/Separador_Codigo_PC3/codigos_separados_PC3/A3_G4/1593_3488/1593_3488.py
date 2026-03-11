from numpy import*

N = array(eval(input("trb: ")))
i = 0
peso = 0
den = 0
num = 0

while (i < size(N)):
	peso = i + 1
	num = num + (N[i] * peso)
	den = den + peso
	i = i + 1
j = num/den
	
print(round(j, 2))