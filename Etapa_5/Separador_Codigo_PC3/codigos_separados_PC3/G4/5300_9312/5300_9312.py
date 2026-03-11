from math import*
velr = float(input(""))
while(velr>50):
	print(round(velr,2))
	velr = velr - 0.25*velr
	
	