nome= input("nome do aminoácido: ")
o = 15.9994
c= 12.011
n= 14.00674
h= 1.00794

if(nome == "ARGININA"):
	peso= (c*6)+(h*15)+(n*4)+(o*2)
else:
	peso= (c*9)+(h*11)+n+(o*3)
print(round(peso,2))