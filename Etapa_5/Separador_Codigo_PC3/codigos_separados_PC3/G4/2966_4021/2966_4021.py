val=27.00
num=int(input("quantidade de ingressos:"))
pro=input("tem direito a promocao? (s/n)")
desc=20/100
if(pro.upper()=="S"):
	vtt=(val*num)*desc
else:
	vtt=val*num
	
print(round(vtt,2))	