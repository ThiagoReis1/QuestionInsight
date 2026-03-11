from numpy import*
v = array(eval(input("vetor: ")))
i = 0

while( i < size(v)):
	if(v[i] <= v[i+1]):
		i = i + 1
		x = "True"
	else:
		x = "False"
	i = i + 1
print(x)