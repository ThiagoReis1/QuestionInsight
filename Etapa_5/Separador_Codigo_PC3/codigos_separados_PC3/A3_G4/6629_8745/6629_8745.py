# faça seu código aqui!
from numpy import*
pe = input("Digite a palavra: ").upper()
i = 0
c = 0
while i < len(pe):
	if pe[i] == 'P':
		print(i)
	i = i + 1
	
if 'P' not in pe:
	print("nao achei")
	