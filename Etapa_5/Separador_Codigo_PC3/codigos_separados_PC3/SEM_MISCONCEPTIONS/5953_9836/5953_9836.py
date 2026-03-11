lanche = 6.00
prato_executivo = 13.50
refrigerante = 3.00

v1= input('(L) se for lanche (P) se for prato executivo:')
v2 = int(input("qtde de lanche ou prato executivo:"))
refrigerante1 = int(input("qtde de refrigerante:"))

if v1=="P":
	total = prato_executivo * v2
	
else:
	total = lanche * v2
	
v3=total+refrigerante1 * refrigerante
print(round(v3,2))