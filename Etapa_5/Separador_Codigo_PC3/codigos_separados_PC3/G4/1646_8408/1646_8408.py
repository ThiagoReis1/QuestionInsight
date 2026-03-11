from numpy import*

val = array(eval(input("valores: ")))
cont= 0

for i in range(size(val)):
	if val[i] <= 50:
		cont = cont + 1
vetap= zeros(cont, dtype = int)

ind = 0

for i in range(size(val)):
	if val[i] <= 50:
		vetap[ind] = i
		ind = ind + 1

print(cont)
print(vetap)