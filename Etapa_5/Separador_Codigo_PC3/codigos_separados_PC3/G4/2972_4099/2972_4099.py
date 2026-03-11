So = int(input("posicao inicial: "))
v = int(input("velocidade: "))
t = int(input("tempo de movimento: "))
S1 = 1000

S = So + (v*t)

if(S > S1):
	resultado = "Sim"
else:
	resultado = "Nao"

print(S)	
print(resultado)