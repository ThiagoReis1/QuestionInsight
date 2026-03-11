volume1=int(input("Volume inicial: "))
volume2=int(input("Volume de agua bombeado: "))
volume3=int(input("Volume de agua que a elfa retira: "))
vol=volume1
soma=0
t=0
while(vol<1000):
	vol=vol+(volume2-volume3)*t
	t=t+1
print(vol)

	