comb= float(input())

if (comb < 17.5):
	a= comb + 10.5
	print(round(a,1))
elif (comb >= 17.5 and comb <=35.0):
	a= comb + 14.0
	print(round(a,1))
elif (comb >=35.0 and comb < 50.0):
	a= comb + 18.6
	print(round(a,1))
else:
	a= comb + 24.5
	print(round(a,1))