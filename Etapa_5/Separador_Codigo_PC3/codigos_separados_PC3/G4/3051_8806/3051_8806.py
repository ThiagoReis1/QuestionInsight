cons = float(input("Informe o seu consumo de energia desse mes: "))

if(cons >= 0 and cons <150):
	vl = (cons*0.60)+5.0
elif(cons >= 150 and cons < 250):
	vl = (cons*0.65)+8.0
elif(cons >= 250 and cons < 350):
	vl = (cons*0.70)+12.0
else:
	vl = (cons*0.75)+16.0
	
print(vl)