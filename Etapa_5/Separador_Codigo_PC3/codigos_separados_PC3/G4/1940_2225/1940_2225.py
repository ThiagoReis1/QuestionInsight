ami= input("Glutamina ou Treonina? ").upper()

if(ami=="GLUTAMINA"):
	C= 12.011
	H= 1.00794
	O= 15.9994
	N= 14.0067
	print(round((C*5)+(H*8)+(N*1)+(O*4),2))
	
else:
	C= 12.011
	H= 1.00794
	O= 15.9994
	N= 14.0067
	print(round((C*4)+(H*9)+(N)+(O*3),2))
	