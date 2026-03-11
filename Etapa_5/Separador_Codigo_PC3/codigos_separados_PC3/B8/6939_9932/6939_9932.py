valortotal = float(input())
codigo = input()
if codigo == 'D' or codigo == 'P':
	valortotal = valortotal - (valortotal*0.19)
	print(round(valortotal,2))
elif codigo == 'C':
	x = int(input())
	if x == 1:
		print(round(valortotal,2))
	else:
		valortotal = valortotal + (valortotal*0.09)
		print(round(valortotal,2))