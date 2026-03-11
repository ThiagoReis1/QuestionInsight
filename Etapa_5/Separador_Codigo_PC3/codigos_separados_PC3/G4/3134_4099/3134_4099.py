from numpy import*
Y = array(eval(input("valores: ")))
i = 0
M = 0
n = size(Y)
while(i < n):
	a = Y[i]**2
	M = M + (a/n)
	i = i + 1

M = M**(1/2)
print(round(M , 2))	