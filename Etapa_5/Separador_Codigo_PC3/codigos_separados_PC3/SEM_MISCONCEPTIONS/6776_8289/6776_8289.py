ano = float(input(":"))
nacao = input(":").upper()

bra = 18
uk = 17

base = 2023

cal = base - ano

if nacao == "B" :
	 cal >= bra 
	print("sim")
	print(cal - bra)
elif nacao == "R":
	cal >= uk 
	print("sim")
	print(cal - uk)
else:
	print("invalido")
	
	