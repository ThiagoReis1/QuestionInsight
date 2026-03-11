con=float(input("consumo de energia:"))

if 0<=con and con<=150:
	v= con*0.60 + 5
	print(round(v,2))
	
if 150<con and con<=250:
	v= con*0.65 + 8
	print(round(v,2))
	
if 250<con and con<=350:
	v= con*0.70 + 12
	print(round(v,2))
	
if con>350:
	v= con*0.75 + 16
	print(round(v,2))