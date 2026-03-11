comum = float(input("insira um numero: "))

if ( 0< comum < 17.5):
	total = comum + 0.8 
	print(round(total, 1))
	
elif( 17.5 < comum < 35):
	total = comum + 1.3
	print(round(total, 1))
	
elif(35< comum< 50):
	total = comum + 2.1
	print(round(total, 1))
	
else: 
	total = comum + 3
	print(round(total, 1))