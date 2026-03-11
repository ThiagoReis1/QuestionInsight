quantidade = float(input())

if(quantidade < 17.5):
	tylium = 10.5
elif(quantidade >= 17.5 and quantidade <35.0):
	tylium = 14.0
elif(quantidade >=35.0 and quantidade <50.0):
	tylium = 18.6
else:
	tylium = 24.5
total = quantidade + tylium
print(round(total,2))