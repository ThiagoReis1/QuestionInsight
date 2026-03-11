nome=input()

o=15.9994
c=12.011
n=14.00674
h=1.0079

if (nome.upper() == "GLICINA"):
	peso= (2*c)+(5*h)+(2*o)+n

else:
	peso= (3*c)+(h*7)+(o*3)+n

print(round(peso,2))
