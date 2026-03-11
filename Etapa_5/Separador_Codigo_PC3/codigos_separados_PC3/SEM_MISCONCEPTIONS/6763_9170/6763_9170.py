# faça seu código aqui!
h = float(input("Digit o tempo: "))
total=5

if h<2:
	total+=1.25
elif h==2:
	total+=2.25
else:
	total+=3.25
	
print(round(total,2))
