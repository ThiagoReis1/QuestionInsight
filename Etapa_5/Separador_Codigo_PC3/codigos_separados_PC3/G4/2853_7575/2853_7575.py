from numpy import*

v=array(eval(input("teste: ")))

n=0

for i in range(size(v)):
	if v[i]==10:
		n=n*10
	else:
		n=n+v[i]
		
print(n)
