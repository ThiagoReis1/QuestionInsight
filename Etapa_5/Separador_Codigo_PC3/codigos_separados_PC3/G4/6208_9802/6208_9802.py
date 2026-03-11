ns = int(input("numero da sorte? "))

cont = 0

while ns != -1:
	if ns >= 51 and ns <= 75:
		cont = cont + 1
	ns = int(input("numero da sorte? "))
print( cont )
		
		
	