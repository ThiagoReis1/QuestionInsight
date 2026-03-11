vo = float(input("Volume inicial: "))
vm = float(input("Volume bombeado para dentro da masmorra por minuto: "))
vr = float(input("Volume retirado a cada minuto: "))

i = 0
t = 0

while (i > 1000):
	i = i + ((vo+vm)-(vr))
	t = t+1
	
print(t)