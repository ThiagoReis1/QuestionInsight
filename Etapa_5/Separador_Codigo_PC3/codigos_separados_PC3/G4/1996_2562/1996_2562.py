x= input("nome do aminodrogas: ").lower()
c= 12.011
o= 15.9994
n= 14.0067
s= 32.066
h= 1.0079
if(x == "aspartato"):
	y=((c*4)+(h*6)+(n)+(o*4))
	print(round(y,2))
elif(x == "fenilalanina"):
	y= ((c*9)+(h*11)+(o*2)+(s))
	print(round(y,2))
elif(x =="tirosina"):
	y= ((c*9)+(h*11)+(n)+(o*3))
	print(round(y,2))
else:
	print("Entrada:",x)
	print("Dado Invalido")