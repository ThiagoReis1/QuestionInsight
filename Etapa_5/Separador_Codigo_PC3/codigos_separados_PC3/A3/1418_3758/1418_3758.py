mais_votado = int(input("o mais votado: "))
segundo_lugar = int(input("segundo mais votado: "))
menos_votado = int(input("menos votado: "))
brancos = int(input("votos em branco: "))
nulos = int(input("votos nulos: "))

s= ((mais_votado + segundo_lugar + menos_votado) / 2)
if(mais_votado>=s):
	print("SIM")

	
else:
	print("NAO")
	