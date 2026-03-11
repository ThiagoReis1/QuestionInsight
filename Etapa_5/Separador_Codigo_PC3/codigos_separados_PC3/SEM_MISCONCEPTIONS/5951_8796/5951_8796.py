escolha = input()
if escolha == "S":
	qtde = int(input()) 
	acai = int(input())
	total = qtde * 5 + acai * 12
else:
	qtde = int(input())
	acai = int(input())
	total = qtde * 4.50 + acai * 12
	
print(round(total, 2))
	
    