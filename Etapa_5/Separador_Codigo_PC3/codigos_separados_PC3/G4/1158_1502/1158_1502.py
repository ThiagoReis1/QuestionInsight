tra = int(input("populaçao de tracajas: "))
taxa = int(input("taxa anual: "))
tr = int(input("numero de tracajas roubados: "))

t = 0
while(tra > 0):
	tra = tra +((taxa *tra)/100)
	tra = tra - tr - 500
	t = t + 1
print(t)