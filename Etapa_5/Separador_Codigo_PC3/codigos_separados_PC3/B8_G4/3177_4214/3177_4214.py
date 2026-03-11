from numpy import *

vet = (array(str(input("palavra:"))))

a= zeros(1,dtype=int)
e= zeros(1,dtype=int)
i= zeros(1,dtype=int)
o= zeros(1,dtype=int)
u= zeros(1,dtype=int)

for i in range(size(vet)):
	if(range(size(vet)) == "a"):
		a[0]= a[0] + 1
	elif(range(size(vet)) == "e"):
		e[0]= e[0] + 1
	elif(range(size(vet)) == "i"):
		i[0]= i[0] + 1
	elif(range(size(vet)) == "o"):
		o[0]= o[0] + 1
	elif(range(size(vet)) == "u"):
		u[0]= u[0] + 1

print("a:",a)
print("e:",e)
print("i:",i)
print("o:",o)
print("u:",u)