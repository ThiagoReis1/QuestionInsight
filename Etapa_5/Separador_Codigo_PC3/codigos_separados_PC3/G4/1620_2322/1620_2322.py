from numpy import*

x = array(eval(input("tempo do banho: ")))
y = array(eval(input("precentual: ")))
i = 0
L = 0
while i < size(x):
	L = L + x[i]*((y[i]/100)*5)
	i = i + 1
print(round(L, 2))
	