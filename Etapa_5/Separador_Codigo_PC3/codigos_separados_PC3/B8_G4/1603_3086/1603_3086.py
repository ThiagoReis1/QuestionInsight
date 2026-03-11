from numpy import*
v = array(eval(input("anel acertado: ")))
i=0
s=0

while(v[i]<4):
	if v[i]== 1:
		s=s+80
		i=i+1
	elif v[i]==2:
		s=s+40
		i=i+1
	elif v[i]==3:
		s=s+20
		i=i+1
		
print(s)	