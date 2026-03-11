peso = float(input())
d = float(input())
cod = float(input())

if cod == 1: 
	s = ((peso*25)+ (d*0.10)) * (1 + 0.17 )
	print(round(s,2))
elif cod == 2:
	s = ((peso*25) + (d*0.10)) * (1+ 0.175)
	print(round(s,2))
elif cod == 3:
	s = ((peso*25) + (d*0.10)) * (1+ 0.18)
	print(round(s,2))
elif cod == 4:
	s = ((peso*25) + (d*0.10)) * (1+ 0.2)
	print(round(s,2))