So=int(input("posicao inicial(m): "))
v=int(input("velocidade(m/s): "))
t=int(input("deslocamento (S): "))
S=So+v*t
print(S)
if(S>1000):
	print("Sim")
else:
	print("Nao")