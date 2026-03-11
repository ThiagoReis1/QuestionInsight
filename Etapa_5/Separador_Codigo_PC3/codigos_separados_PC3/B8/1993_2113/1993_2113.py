am=input("digite o nome do aminoacido: ").lower()
o=15.9994
c=12.011
n=14.0067
s=32.066
h=1.00794
cisteina=(c*3+h*7+n+o*2+s)
isoleucina=(c*6+h*13+n+o*2)
metionina=(c*5+h*11+n+o*2+s)


if(am!="cisteina" and am!="isoleucina" and am!="metionina"):
	print("Entrada: ",am)
	print("Dado invalido")
elif(am=="cisteina"):
	print(round(cisteina,2))
elif(am=="isoleucina"):
	print(round(isoleucina,2))
elif(am=="metionina"):
	print(round(metionina,2))
	
