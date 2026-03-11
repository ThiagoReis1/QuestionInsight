from numpy import*

dado = array(eval(input("digite o vetor: ")))


s = 200
i = 0 
while i < size(dado):
	if dado[i] == 1:
		s = s/2
		
	elif dado[i] == 2:
		s = s*3
	
	elif dado[i] == 3:
		s = s/2
		
	elif dado[i] == 4:
		s = s * 3 
	elif dado[i] == 5:
		s = s/2 
		
	elif dado[i] == 6:
		s = s*3
		
	i = i + 1 
print(round(s, 2))