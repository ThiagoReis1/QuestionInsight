# faça seu código aqui!
idade_espectador = int(input("idade dos espectadores"))

if idade_espectador == 12:
	taxaad = 20.0 +  2.25
elif idade_espectador < 12:
	taxaad = 20.0 + 1.25
elif idade_espectador > 12:
	taxaad = 20.0 + 3.25
print(round(taxaad,2))
	
	