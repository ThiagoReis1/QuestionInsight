lanche = 6.00
pratoexecutivo = 13.50
refri = 3.00

x = input("(L) se for lanche (P) se for prato executivo: ")
b = int(input("insira quantidade de lanches ou pratos: "))
quanre = int(input("insira refris: "))

if x == "L":
	total = lanche * b
else:
	total = pratoexecutivo * b
		  
pf = total + quanre * refri
print(pf)