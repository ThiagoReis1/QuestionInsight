S0=int(input("qual a posicao inicial do objeto(m)?"))
V=int(input("qual a valocidade do objeito(m/s)?"))
T=int(input("qual o tempo de deslocamento(s)?"))
S=S0+V*T
if(V<=100):
	mensagem = "OK"
else:
	mensagem = "ACIMA"
print(S)
print(mensagem)