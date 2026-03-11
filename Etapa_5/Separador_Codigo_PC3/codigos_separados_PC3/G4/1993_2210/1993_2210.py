m=input("entre com a molecula: ").lower() 

O=15.9994
C=12.011
N=14.0067
S=32.066
H=1.00794


Ci=(C*3)+(H*7)+(N)+(O*2)+(S)
Is=(C*6)+(H*13)+(N)+(O*2)
Me=(C*5)+(H*11)+(N)+(O*2)+(S)

if(m=="cisteina"):
	print(round(Ci,2))
elif(m=="isoleucina"):
	print(round(Is,2))
elif(m=="metionina"):
	print(round(Me,2))
else:
	print("Entrada:",m)
	print("Dado Invalido")
