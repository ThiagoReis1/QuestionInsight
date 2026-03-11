a = int(input("Digite a quantidade de pontos de força de cada guerreiro: "))
b = int(input("Digite a quantidade de pontos incial de pontos de força do troll: "))
c = int(input("Digite a quantidade de pontos de força que o troll recupera: "))

t = 0 

while (b > 0): 
	b =  b - a*5 + c 
	t=t + 1 

print(t)
		