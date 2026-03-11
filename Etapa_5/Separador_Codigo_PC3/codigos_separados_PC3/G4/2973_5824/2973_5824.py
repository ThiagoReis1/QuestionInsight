s0=int(input("posicao inicial: "))
v=int(input("velocidade do objeto: "))
t=int(input("tempo: "))
s=(s0+v*t)
print(s)
if(v<=100):
	print("OK")
if(v>100):
	print("ACIMA")