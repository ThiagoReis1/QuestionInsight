qi = int(input("pontos de vida:"))
v1 = int(input("primeiro:"))
v2 = int(input("segundo:"))
v3 = int(input("terceiro:"))
dano = int(input("dano:"))

pdr = qi - dano
print(pdr)
if (pdr>130):
	resultado = "VIVO"
elif (pdr<130):
   resultado = "MORTO"
else:
	(130<pdr)
	resultado = "invalido"
	
print(resultado)
	

	
