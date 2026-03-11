#UNIVERSIDADE FEDERAL DO AMAZONAS
#GRADUACAO EM GEOLOGIA BACHARELADO
#ALUNO: WILLIAM NUNES SANTOS - MATRICULA 21852890

#AVALIACAO - QUESTAO 01

tempo = float (input("Digite o tempo em minutos:"))
tarifafixa = 25.00

if (tempo <= 100):
	valor = (1.20 * tempo) 
else:
	valor = ((1.40 * tempo) + 25.0)
	
print (round(valor,2))
