tot = float(input())
cd = input().upper()
if(cd==("D" or "P")):
	x = tot-(tot*0.11)
else:
	if(cd=="C"):
		a1 = float(input())
		if(a1 == 1):
			x = tot
		else:
			x = tot+(tot*0.06)
print(round(x, 2))
		
		