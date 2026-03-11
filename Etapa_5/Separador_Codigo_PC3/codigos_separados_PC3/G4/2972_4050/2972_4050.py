so = int(input("digite um valor da posicao: "))
v = int(input("digite o valor da velocidade: "))
t = int(input("digite o valor do tempo: "))
S = so + v*t
print(S)
if(S >= 1000):
	print("Sim")
else:
	print("Nao")