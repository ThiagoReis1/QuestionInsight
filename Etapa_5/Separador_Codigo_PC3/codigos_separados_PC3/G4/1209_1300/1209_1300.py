from numpy import*
r = 74.08
	
x = array(eval(input("digite as quatidades: ")))
i = 0
j = 0
while(i<size(x)):
	if(x[i]>r):
		j = j + 1
	i = i + 1
print(r)
print(j)