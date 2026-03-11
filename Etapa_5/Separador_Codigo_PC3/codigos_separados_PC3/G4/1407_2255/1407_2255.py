pv = int(input("pontos de vida: "))
d1 = int(input(": "))
d2 = int(input(": "))
d3 = int(input(": "))
N = pv-((d1+d2+d3)*10) 
if(N < 0):
	mensagem1 = 0
	mensagem2 = "vivo"
	
else:
	mensagem1 = 0
	mensagem2 = "morto"
print(mensagem1)
print(mensagem2)