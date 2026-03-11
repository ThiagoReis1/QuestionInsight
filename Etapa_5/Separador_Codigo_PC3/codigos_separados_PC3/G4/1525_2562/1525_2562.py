vi= int(input("Volume inicial: "))
bd= int(input("Volume bombeado para dentro: "))
vr= int(input("Volume que a elfa retira:"))

k=	vi
t= -10 	#minutos

while(k>0):
	k=k+bd-vr
	t=t+1
	
print(t)
	