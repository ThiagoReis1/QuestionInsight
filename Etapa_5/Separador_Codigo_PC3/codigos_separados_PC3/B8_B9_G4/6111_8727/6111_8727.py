q= int(input("quantidade de combustivel comum:"))

if (q<17.5):
	t= q+10.5
elif (q>=17.5) and (q<35.0):
	t= q+14.0	
elif (q>=35.0)	and (q<=50.0):
	t= q+18.6
elif (q>=50.0):
	t= q+ 24.5
print(round(t,1))