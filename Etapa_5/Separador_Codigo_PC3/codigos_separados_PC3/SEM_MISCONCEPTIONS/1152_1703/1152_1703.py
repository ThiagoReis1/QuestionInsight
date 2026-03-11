# Hanna Soares Rodrigues - 21650885
# Avaliacao 04
# Exercicio 04

bravos = int(input("Numero habtantes bravos: "))
pentos = int(input("Numero habtantes pentos: "))
porto_real = int(input("Numero habtantes porto real: "))
taxa_bravos = float(input("Taxa anual de crescimento de bravos: "))
taxa_pentos = float(input("Taxa anual de crescimento de pentos: "))
taxa_preal = float(input("Taxa anual de crescimento de porto real: "))

contador = 0
t_bravos = taxa_bravos/100
t_pentos = taxa_pentos/100
t_preal = taxa_preal/100
soma = 0

while (soma >= porto_real):
	porto_real = porto_real + (porto_real*t_preal)
	soma = (bravos + (bravos*t_bravos)) + (pentos + (pentos*t_pentos))
	contador = contador + 1																			  
																			  
print(contador)
