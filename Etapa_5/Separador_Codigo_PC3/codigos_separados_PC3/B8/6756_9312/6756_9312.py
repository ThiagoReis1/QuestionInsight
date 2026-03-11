from math import*
dia = int(input(""))
if(dia<15):
	total = 175*dia + 20
elif(dia == 15):
	total = 175*dia + 16
elif(dia>15):
	total = 175*dia + 10
print(round(total,2))

	
	