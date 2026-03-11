kwh=float(input())
v1=(kwh*0.60)+5
v2=(kwh*0.75)+16
if (kwh<=150):
	print(round(v1,2))
if(kwh>=150):
	print(round(v2,2))