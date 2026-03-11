qi = int(input("Quantidade inicial de grifos: "))
x = int(input("Quantidade de novos grifos treinados(a cada trimestre): "))
y = int(input("Quantidade de grifos contaminados(a cada trimestre):"))

t = 0
g = qi
gt = 400
while(g > 0 and g < gt):
	g = g + x - y
	t = t + 1
	
print(t)