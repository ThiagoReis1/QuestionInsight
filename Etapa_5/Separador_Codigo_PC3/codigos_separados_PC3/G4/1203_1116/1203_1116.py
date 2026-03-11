from numpy import*
r = array(eval(input("Altura pulada: ")))

a = 2.5
i = 0
j = 0
while(i < size(r)):
	if(r[i] > a):
		j = j + 1
	i = i + 1
print(a)
print(j)
	