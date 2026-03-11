m = int(input("numero de macas compradas: "))

#caso compre menos de uma duzia

#mais de uma duzia ou mais

total = 0

if m < 12:
	total = m * 0.30
else:
	total = m * 0.25
	

	
print(round(total, 2))
