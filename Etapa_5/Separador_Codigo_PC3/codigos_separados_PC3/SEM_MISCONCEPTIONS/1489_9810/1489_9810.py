e= float(input())
if (0=e<150):
	v= e*0.60+5
elif (150<=e<=250):
	v= e*0.65+8
elif(250<=e<=350):
	v= e*0.70+12
elif (e>350):
	v=e*0.75+16
print(round(v,2))