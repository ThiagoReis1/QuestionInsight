amin= input("Asparagina ou Triptofano? ").upper()

o = 15.999
c = 12.011
n = 14.00674
h = 1.00794

if(amin == "Asparagina".upper()):
	peso = c*4 + h*8 + n*2 + o*3
	print(round(peso,2))
else:
	peso2= c*11 + h*11 + n*2 + o*2
	print(round(peso2,2))