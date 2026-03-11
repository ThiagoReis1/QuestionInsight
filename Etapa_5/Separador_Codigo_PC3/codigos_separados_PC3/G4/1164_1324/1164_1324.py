n=int(input("Digite a quantidade de termos:"))

vc = 0
va = 0
pa = 0

while vc>n:
	if(pa%2==0):
		pa+=((vc+1)**2)/(4+(va+1))
		vc+=1
		va+=2
	else:
		pa-=((vc+1)**2)/(4+(va+1))
		vc+=1
		va+=2
