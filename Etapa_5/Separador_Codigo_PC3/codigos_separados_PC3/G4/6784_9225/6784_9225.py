v1 = int(input("digite seu ano de nascimento: "))
v2 = input("digite lugar de origem: ")
x = v2.upper()
v3 = 2023 - v1

if v3>=21 and x=="B":
	print("sim") 
	print(v3-21)

elif v3>=18 and x=="R":
	print("sim")
	print(v3-18)

elif v3<21 and x=="B":
	print("nao")
	print(21 - v3)
	
elif v3<18 and x=="R":
	print("nao")
	print(18 - v3)
	
else:
	print("invalido")
	






	