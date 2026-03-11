a=input("nome do aminoacido: ")
o=15.999
c=12.011
n=14.00674
h=1.00794
histidina=(c*6)+(h*10)+(n*3)+(o*2)

prolina=c*5+h*10+n+o*2

if(a.lower()=="histidina"):
	print(round(histidina,2))
	
else:
	print(round(prolina,2))