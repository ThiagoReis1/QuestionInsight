cg = int(input("a quantidade de pontos de força que cada guerreiro tira do troll:"))
i = int(input("A quantidade inicial de pontos de força do troll:"))
t = int(input("a quantidade de pontos de força que o troll recupera:"))
va = 0
while(i>0):
	i = i - (cg*5)+t
	va= va+1
print(va)
	