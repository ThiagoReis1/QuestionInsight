c = float(input("conaulmo de agua: "))
taxa = 30
if  c < 10:
	x = (3 * c) + taxa 
else:
	x = taxa + (3.5*c)
print(round(x,2))