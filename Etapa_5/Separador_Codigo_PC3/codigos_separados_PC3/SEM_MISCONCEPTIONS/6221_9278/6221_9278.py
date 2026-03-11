valor_x = int(input("digite valor de x: "))
valor_y = int(input("digite valor de y: "))

s = 0

while valor_x <= valor_y:
	if valor_y % 7 == 0:
		s = s + valor_y
		
	valor_y = valor_y - 1
print(s)	
	
	
	
	