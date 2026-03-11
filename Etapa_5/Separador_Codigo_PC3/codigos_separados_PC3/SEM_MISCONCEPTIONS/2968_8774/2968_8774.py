escolha_ls= input()
if escolha_ls.upper() == "L":
	qtde_l = int(input())
	refri = int(input())
	valor = qtde_l * 5. + refri * 4.
else:
	qtde_s = int(input())
	refri = int(input())
	valor = qtde_s * 3.50 + refri * 4
print(valor)

