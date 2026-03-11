from numpy import*
v = array(eval(input("Digite os saltos: ")))
i = 0
k = 0
r = 2.5

while(i < size(v)):
	if(v[i]<r):
		k = k + 1
	i = i + 1
		
print(r)
print(k)	