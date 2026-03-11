
idade=int(input("Digite a ano: "))
pais=input("Digite o pais: ").upper()
requisito=2023-idade



if pais=="B" and requisito>=21:
	print("sim")
	print(requisito-21)
elif pais=="B" and requisito<21:
	print("nao")
	print(21-requisito)
elif pais=="E" and requisito>=18:
	print("sim")
	print(requisito-18)
elif pais=="E" and requisito<=18:
	print("nao")
	print(18-requisito)
else:
	print("invalido")
	
