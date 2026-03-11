# faça seu código aqui!
integr = int(input("Numero de alunos integrantes: "))
nome_candidato = input("Nome do professor: ").lower()
c = 0
acmt = 0
acme = 0
acma = 0

while (c < integr):
	nome_candidato = input("Nome do professor: ").lower()
	if (nome_candidato == "tais" or nome_candidato == "edgar" or nome_candidato == "ana"):
		c = c + 1
		
	if (nome_candidato == "tais"):
		acmt = acmt + 1
	elif(nome_candidato == "edgar"):
		acme = acme + 1
	elif(nome_candidato == "ana"):
		acma = acma + 1
		
print("tais=" ,acmt).lower()
print("edgar=" ,acme).lower()
print("ana=" ,acma).lower()