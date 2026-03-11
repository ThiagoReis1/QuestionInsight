from math import*

x=input()
aux = x
x=  x.lower()
o=15.999
c=12.011
n=14.00674
h=1.00794

g=(c*5)+(h*8)+(o*4)+(n*1)
h=(c*6)+(h*10)+(n*3)+(o*2)
p=(c*5)+(h*10)+(o*2)+(n*1)

if(x=="glutamina"):
	print(round(g,2))
elif(x=="histidina"):
	print(round(h,2))
elif(x=="prolina"):
	print(round(p,2))
else:
	print("Entrada:",aux)
	print("Dado Invalido")