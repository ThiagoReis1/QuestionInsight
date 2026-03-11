maisV = int(input("Digite o candidato mais votado:"))
segundoL = int(input("Digite o candidato do segundo lugar:"))
menosV = int(input("Digite o candidato menos votado:"))
brancos = int(input("Digite os votos em brancos:"))
nulos = int(input("Digite os votos em brancos:"))

if(maisV > 2000)and(maisV != brancos) and(maisV!=nulos):
	print("SIM")
elif(maisV == 2000) or (sgundoL < 2000) or (menosV != 2000) :
	print("NAO")
else:
	print("ERRO")
