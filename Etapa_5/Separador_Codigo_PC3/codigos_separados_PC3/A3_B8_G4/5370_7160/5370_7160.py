from numpy import*

v = array(eval(input(":")))

i = 0
j = 1
tamanho = len(v)
a = 0

while (j < tamanho):
	if (v[i] > v[j]):
		i = i + 1
		j = j + 1
		a = 0
		break
	elif (v[i] <= v[j]):
		i = i + 1
		j = j + 1
		a = a + 1
		
if (a >= 1):
	print("True")
else:
	print("False")
	
		
	
	
		
