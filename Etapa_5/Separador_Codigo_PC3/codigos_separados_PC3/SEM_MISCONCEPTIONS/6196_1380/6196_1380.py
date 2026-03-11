altura_chico = 1.5
taxa_chico = 0.02

altura_fulano = float(input("Informe a altura do outro aluno: "))
taxa_fulano = float(input("Informe a taxa de crencimento do outro aluno: "))

anos = 0

while (altura_fulano < altura_chico):
	anos += 1
	altura_fulano += taxa_fulano
	altura_chico += taxa_chico

print(anos)