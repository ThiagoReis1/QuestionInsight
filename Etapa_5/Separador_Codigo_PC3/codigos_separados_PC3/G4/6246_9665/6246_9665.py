r = input("digite o resultado: ").upper()

cont = 0

while r != "X":
	if r == "A":
		cont = cont + 1
	r = input("digite o resultado: ").upper()
	
print(cont)