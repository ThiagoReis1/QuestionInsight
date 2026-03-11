from numpy import * 
notas=array(eval(input("notas: ")))
maxi=notas[:max(notas)]
mfinal=(maxi)/3
if(mfinal<=5):
	print("APROVOU")
else:
	print("REPROVOU")
print(round(mfinal,2))