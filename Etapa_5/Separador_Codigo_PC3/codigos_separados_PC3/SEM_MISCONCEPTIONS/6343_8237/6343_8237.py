from numpy import*

vetor = input("Digite um valor:")

if (vetor[1] == "a") or (vetor[1] == "A"):
	nome = vetor.upper()
	print(nome)
else:
	msg = "nome invalido"
	print(msg)