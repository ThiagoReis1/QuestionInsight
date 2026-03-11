from numpy import *
dp=array(eval(input("QUAL:")))
m= sum(dp)
pt= (m-min(dp))/3.0
print(round(pt,2))
if(pt>=50):
	print("APROVADO")
else:
	print("REPROVADO")
	