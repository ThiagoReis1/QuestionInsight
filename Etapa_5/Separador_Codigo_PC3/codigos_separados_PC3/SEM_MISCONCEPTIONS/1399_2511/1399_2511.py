#Segundo turno

voto_ambrosio = float(input("Digite a quantidade de votos: "))
voto_demelza = float(input("Digite a quantidade de votos: "))
total_de_votos = voto_ambrosio + voto_demelza

if(voto_ambrosio>voto_demelza):
	porcentagem = voto_ambrosio / total_de_votos * 100
	print("Ambrosio Rutra")
	print(round(porcentagem,2))
else:
	porcentagem = voto_demelza/ total_de_votos * 100
	print("Demelza Olecram")
	print(round(porcentagem,2))