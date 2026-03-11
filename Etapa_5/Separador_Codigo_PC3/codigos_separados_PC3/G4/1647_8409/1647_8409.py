from numpy import*

por = array(eval(input("porc")))
cont = 0
for i in range (size(por)):
	if p[i] >= 70:
		cont = cont + 1
vetap = zeros(cont,dtype = int)
ind = 0
for i in range (size(por)):
	if por[i] >= 70:
		vetap[ind] = i
		ind = ind + 1

print(cont)
print(vetap)