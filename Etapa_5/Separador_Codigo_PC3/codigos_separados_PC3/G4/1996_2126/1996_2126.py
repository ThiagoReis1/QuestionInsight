a = input("Nome do aminoacido :").lower()
z = ((9*12.011)+(11*1.0079)+(2*15.994)+(32.066))
y=((9*12.011) + (1.0079*11) + 14.0067 + (3*15.9994))
x=((4*12.011)+(1.0079*6)+14.0067+(4*15.9994))
if(a =="fenilalanina"):
	print(round(z,2))
elif(a =="tirosina"):
	print(round(y,2))
elif(a=="aspartato"):
	print(round(x,2))
else:
	print("Entrada:",a)
	print("Dado Invalido")
