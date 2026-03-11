# Leitura de variáveis
nome = input("Insira o nome do aminoácido: ")

O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

if(nome.lower() == "aspartato"):
	peso = 4*C + 6*H + N + 4*O
	
if(nome.lower() == "cisteina"):
	peso = 3*C + 7*H + N + 2*O + S
	
print(round(peso,2))

