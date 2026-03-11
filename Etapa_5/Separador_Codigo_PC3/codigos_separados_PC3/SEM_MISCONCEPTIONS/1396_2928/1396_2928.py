valorc = float(input())

if(valorc <= 300):
	gorjeta = valorc*0.10
else:
	gorjeta = valorc*0.06
	
valort = valorc+gorjeta
print(round(valort,2))