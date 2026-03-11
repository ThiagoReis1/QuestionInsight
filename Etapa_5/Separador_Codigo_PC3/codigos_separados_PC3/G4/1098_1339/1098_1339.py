N=int(input("numero: "))
X=N//1000
Y=N%1000
Z=(X-Y)**4
if(N==Z):
	print(N,"atende a propriedade")
else:
	print(Z)
 
