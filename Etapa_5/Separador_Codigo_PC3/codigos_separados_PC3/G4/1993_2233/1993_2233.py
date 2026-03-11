a=input("aminoacido")
o=15.9994
c=12.011
n=14.0067
s=32.066
h=1.00794
A=(a).lower()

if(A=="cisteina"):
	cis=((c*3)+(h*7)+(n)+(o*2)+(s))
	print(round(cis,2))
elif(A=="isoleucina"):
	iso=((c*6)+(h*13)+(n)+(o*2))
	print(round(iso,2))
elif(A=="metionina"):
	met=((c*5)+(h*11)+(n)+(o*2)+(s))
	print(round(met,2))
else:
	print("Entrada:",a)
	print("Dado Invalido")
	
	


