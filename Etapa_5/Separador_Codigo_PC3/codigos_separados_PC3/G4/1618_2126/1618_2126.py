from numpy import*
v = array(eval(input("v:")))
i = 0
j = (size(v)-1)
vet = ""
while(size(v)>i):
	i= i+1
	j = j-1
	vet = vet + str(v) + "x^" + str(j)
print(vet)





