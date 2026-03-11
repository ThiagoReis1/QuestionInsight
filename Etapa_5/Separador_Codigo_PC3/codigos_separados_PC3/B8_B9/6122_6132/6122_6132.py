qcc = float(input("quantidade de combustivel comum (qcc>0): "))

if (qcc<17.5):
	total = qcc + 0.8
elif (qcc>=17.5) and (qcc<35):
	total = qcc + 1.3
elif (qcc>=35) and (qcc<50):
	total = qcc + 2.1
elif (qcc>=50):
	total = qcc + 3
	
print(round(total,1))