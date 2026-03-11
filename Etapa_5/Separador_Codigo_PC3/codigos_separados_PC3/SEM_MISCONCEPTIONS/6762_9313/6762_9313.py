idade=int(input("idade: "))

if idade<12:
	v=20+1.25
	print(round(v,2))
elif idade==12:
	v=20+2.25
	print(round(v,2))
else:
	v=20+3.25
	print(round(v,2))