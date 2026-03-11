from numpy import*

custo = array(eval(input("custo: ")))

i = 0
v = 0
 
while i < size(custo):
	if custo[i] > 80.0:
		v[i] = v + 1 
	i = i + 1
total = v // 0.15	
print(total)	
	
		
		