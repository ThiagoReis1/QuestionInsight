cachos = int(input("numero de cachos: "))
total = 0
if(cachos < 3):
	total = cachos*5
else:
	total = cachos*4.25
	
print(round(total,2))	