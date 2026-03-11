from numpy import*
v = array(eval(input("digite a temperatura: ")))
i = 0
j = 0
while(i<size(v)):
	if(v[i] > 10):
		j = j + 1
	i = i + 1
print(j)