v = input("Digite uma string:").upper()
x1 = 7.25
x2 = 4.75
x3 = 3.50

x = 0
i = 0

while(i < len(v)):
	if (v[i] == 'M'):
		x = x + x1
		
		
	elif( v[i] == 'P'):
		x = x + x2
		
		
	 
	elif( v[i] == 'R'):
		x = x + x3
	
	i = i + 1	
print(round(x,2))
		