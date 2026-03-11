o=15.999
c=12.011
n=14.00674
h=1.00794
aminoacido=input("aa: ")
if(aminoacido.upper() == "ASPARAGINA"):
	asparagina=((12.011*4)+(1.00794*8)+(14.00674*2)+(15.999*3))
	print(round(asparagina,2))
else:
	triptofano=((12.011*11)+(11*1.00794)+(2*14.00674)+(2*15.999))
	print(round(triptofano,2))
					