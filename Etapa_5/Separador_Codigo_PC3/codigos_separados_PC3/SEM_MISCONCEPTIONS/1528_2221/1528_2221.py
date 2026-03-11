from numpy import*

am=int(input("digite a qtd inicial: "))
br=int(input("digite a qtd inicial: "))
el=int(input("digite a qtd inicial: "))     
troll=br
rodada=0

while(troll > 0):
	troll = troll - 5*am
	troll = troll + el
	rodada = rodada + 1

print(rodada)