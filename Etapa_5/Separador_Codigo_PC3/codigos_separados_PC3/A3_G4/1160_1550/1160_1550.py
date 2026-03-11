h= int(input("digite o numero de habitantes: "))
v= int(input("digite o numero de vampiros: "))
x= int(input("digite o numero de pessoas transformadas: "))
y= int(input("digite o numero de vampiros mortos: "))
dias = 0
vampiros = 0
while(v<=h):
	soma=(h-(v*x*y))-v
	dias=dias+1
print(dias)

