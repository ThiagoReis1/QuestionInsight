x  = float(input("Ler numero real: "))
k = int(input("Ler qtd de termos desejados: "))

cont = 0
ac = 0
den = 1

while(cont < k):
	ac = ac + (-1) ** (cont) * ((x ** den) / den)
	cont = cont + 1
	den = den + 2
print(round(ac, 6))