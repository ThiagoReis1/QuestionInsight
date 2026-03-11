x=input("digite:").lower()

a=(4*12.011)+(6*1.00794)+(1*14.0067)+(4*15.9994)
b=(3*12.011)+(7*1.00794)+(1*14.0067)+(2*15.9994)+(1*32.066)
c=(5*12.011)+(11*1.00794)+(1*14.0067)+(2*15.9994)+(1*32.066)


if(x=="aspartano"):
	print(round(a,2))
elif(x=="cisteina"):
	print(round(b,2))
elif(x=="metionina"):
	print(round(c,2))
else:
	print("Entrada:", x)
	print("Dado Invalido")