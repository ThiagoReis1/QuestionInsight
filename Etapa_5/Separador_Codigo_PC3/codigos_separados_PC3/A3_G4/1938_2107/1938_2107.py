#arginina c6h15n4o2
#tirosina c9h11no3


o = 15.9994
c = 12.011
n = 14.00674
h = 1.00794 

mol =  input("deus me dibre: ")

if(mol.upper() == "ARGININA"):
	nume = c*6 + h*15 + n*4 + o*2
	
if(mol.upper() == "TIROSINA"):
	nume = c*9 + h*11 + n + o*3
	
print(round(nume,2))