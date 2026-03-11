valor = float(input())
opcao = input().upper()

if opcao in ["D", "P"]:
	final = valor*(100-17)/100
elif opcao == "C1":
	final = valor
elif opcao == "C2":
	final = valor*(100+8)/100
print(round(final, 2))