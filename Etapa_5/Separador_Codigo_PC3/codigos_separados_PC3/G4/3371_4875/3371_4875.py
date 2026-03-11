m=input('m=')
v=float(input('v='))
if(m.upper()=='M'):
	print(round(v*(1.60934),2))
else:
	print(round(v/(1.60934),2))