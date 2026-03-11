m=int(input("numero das mangas: "))

if m<6:
	v=(3.80)*m
else:
	v=(3.45)*m
	
print(round(v,2))