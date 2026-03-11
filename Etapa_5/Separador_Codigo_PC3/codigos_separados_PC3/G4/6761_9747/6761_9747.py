v = float(input())
fixo = 60 
if v<50:
	p = 4.5
elif v==50:
	p = 5.5
else:
	p = 6.5
total = fixo + p
print(round(total,2))