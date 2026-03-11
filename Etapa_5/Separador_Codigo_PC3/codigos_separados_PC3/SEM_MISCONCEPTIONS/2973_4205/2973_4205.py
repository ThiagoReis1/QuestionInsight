Si= int(input("digite a a posicao inicial:"))
v=int(input("velocidade do carro:"))
t=int(input("tempo de deslocamento"))
S=Si+v*t
if(S==100)
   posifinal=S
	mensagem ="OK"
else:
	mensagem ="ACIMA"
print(S)
print(mensagem)