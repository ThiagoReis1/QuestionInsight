v0=int(input("volume inicial: "))
va=int(input("volume de agua bombeado para dentro: "))
vb=int(input("volume de agua retirado: "))


m=0

while(v0>1000):
	v0=v0-vb+va
	m=m+1
print(m)
	
	