o = 15.9994
c = 12.011
n = 14.00674
h = 1.00794
alanina = 3*c + 7*h + n + 2*o
valina = 5*c + 11*h + n + 2*o
nome = input()
if (nome == "ALANINA"):
	mensagem = alanina
else:
	mensagem = valina
print(round(mensagem,2))
