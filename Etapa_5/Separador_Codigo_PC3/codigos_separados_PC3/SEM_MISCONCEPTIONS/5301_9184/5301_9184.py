from numpy import *

velocidade = int(input("Digite o valor da velocidade em RPM: "))

tempo_s = 0

while velocidade > 40:
	velocidade -= velocidade * 0.02
	tempo_s += 1
	
print(tempo_s)