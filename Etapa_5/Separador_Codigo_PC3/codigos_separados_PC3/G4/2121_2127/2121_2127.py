from numpy import*
n=array(eval(input("valor:")))
nf=((n*5)+(n*3)+(n*2)/10)
print(round(nf,2))
if(nf>5):
	  print("APROVADO")
else:
	  print("REPROVADO")
