x= floa
V= input("vitorias")
E= input("empates")
D=input("derrotas")
 
t=0
while(t < x):
	V=3*x
	E=1*x
	D= 0*x
t=t+1
if(x==3):
	print(V)
elif(x==1):
	print(E)
else:
	print(D)