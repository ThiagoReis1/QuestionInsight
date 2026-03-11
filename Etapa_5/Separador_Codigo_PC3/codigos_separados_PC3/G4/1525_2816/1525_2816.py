vi= int(input("Volume inicial: "))
vb= int(input("Volume bombeado: "))
vr= int(input("Volume retirado: "))

t=0
v=vi

while(v>1000):
	
	v=v + vb - vr
	t=t + 1
	
print(t)