nom = input("digite o nome do aminoacido:")
O=15.9994
C=12.011
N=14.0067
S=32.006
H=1.00794
pm1 =(4*C)+(H*6)+ N +(O*4)
pm2=(C*3)+(H*7)+ N +(O*2)+(S)
if(nom=="aspartato"):
	print(round(pm1,2))

else:
   print(round(pm2,2))