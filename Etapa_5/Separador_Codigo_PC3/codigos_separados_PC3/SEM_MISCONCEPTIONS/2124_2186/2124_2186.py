from numpy import *
vet=array(eval(input("digite as notas: ")))

sum(vet)-max(vet)
		
MFinal = (sum(vet)-max(vet)) / 3.0
	
print(round(MFinal,2))
if(MFinal>=5):
		print("APROVOU")
else:
		print("REPROVOU")