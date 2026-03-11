#combo float(input("manha energetica"))
cafe= int(input("cafe"))
if cafe >= 4:
	t = 20*cafe-(20*cafe*0.15)
else:
	t = 20*cafe
	
print(round(t, 2))
