from numpy import*
v = array(eval(input("digite a distancia: ")))
i = 0
j = 0
while(i<size(v)):
	if(v[i] < 8.95):
		j = j + 1
	i = i + 1
print("8.95")
print(j)