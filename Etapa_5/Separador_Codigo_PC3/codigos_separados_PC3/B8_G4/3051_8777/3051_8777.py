a = float(input(":"))
if a >0 and a <= 150:
	vc= a*0.60+5.00
elif a> 150 and a<=250:
	vc= a*0.65+8.00
elif a> 250 and a<=350:
	vc= a*0.70+12.00
elif a> 350:
	vc= a*0.75+16.00
print(round(vc, 2))