from numpy import*

v = array(eval(input("Diga: ")))

n = int(input())

i = 0
cont = 0

while (i < size(v)):
	if (v[i] == n):
		print(i)
		
	if(v[i] < n):
		cont = cont + 1
		
		
	i = i + 1
		
print(cont)

	