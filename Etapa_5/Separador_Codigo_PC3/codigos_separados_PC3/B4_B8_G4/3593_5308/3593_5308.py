from numpy import*

dado = array(eval(input("dado:")))

comp = 200

i = 0

while i < size(dado):
	if dado[i] == 1:
		comp = comp / 2
		
	elif dado[i] == 2:
		comp = comp * 3
		
	elif dado[i] == 3:
		comp = comp / 2
		
	elif dado[i] == 4:
		comp = comp * 3
		
	elif dado[i] == 5:
		comp = comp / 2
		
	elif dado[i] == 6:
		comp = comp * 3
	i = i + 1
print(round(comp, 2))
