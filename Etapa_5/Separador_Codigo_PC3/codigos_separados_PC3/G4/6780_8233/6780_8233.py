a=int(input("ano que nasceu:"))
p=input("pais de nascimento:")
i=2023-a
if(p.upper()=="B"):
	if(i<21):
		print("nao")
		print(21-i)
	else:
		print("sim")
		print(i-21)
elif(p.upper()=="C"):
	if(i<24):
		print("nao")
		print(24-i)
	else:
		print("sim")
		print(i-24)
else:
	print("invalido")