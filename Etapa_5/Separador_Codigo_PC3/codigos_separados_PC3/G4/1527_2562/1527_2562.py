qf= int(input("seguidores de Forseti: "))
ql= int(input("seguidores de Loki: "))
pf= float(input("percentual Forseti: "))
pl= float(input("percentual Loki: "))

z= 0
c= 0

t= 0

while(ql <= qf):
	if(z >= c):
		z= z+ qf*pf/100
		c= c+ ql*pl/100
		
	else:
		t= t + 1
		print(t)