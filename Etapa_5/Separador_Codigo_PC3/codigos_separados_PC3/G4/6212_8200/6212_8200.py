num = int(input('qual valor(OUT): '))
ctd = 0
while num > 0:
	if num >= 26 and num <= 85:
	  ctd += 1
	num = int(input('qual valor(IN): '))
print(ctd)