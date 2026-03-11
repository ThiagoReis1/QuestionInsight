from numpy import*
x = array(eval(input("Tempo de chegada: ")))
#print(max(x))
i=0
while i<size(x)-1:
	if x[i]==max(x):
		a=i
	i=i+1
print(a)