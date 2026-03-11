
qi = int(input("quantidade inicial: "))
x = int(input("quantidade x a cada trimestre: "))
y = int(input("quantidade de grifos contaminados: "))

t = 0
while(qi > 0):
	qi = (qi + x) - y
	t = t + 1
print(t)
	
	
