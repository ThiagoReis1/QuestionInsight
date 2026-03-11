a = int(input("insira o ano de nascimento: "))
b = input("insira o pais : ").upper()

total = 2023 - a 
x = total - 18
y = total - 17

B = 18 - total
R = 17 - total 

if b == "B":
	if total >= 18:
		print("sim")
		print(total-18)
	else:
		print("nao")
		print(18-total)
		
elif b == "R":
	if total >= 17:
		print("sim")
		print(total-17)
	else:
		print("nao")
		print(17-total)
else:
	print("invalido")