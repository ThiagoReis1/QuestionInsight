from numpy import*

j = array(eval(input("Digite um numero: ")))

for i in range(size(j)):
	if(j[i] == 9):
		sucessor = 0
	else: 
		sucessor = j[i] + 1
	
	j[i] = sucessor**3
	
print(j)