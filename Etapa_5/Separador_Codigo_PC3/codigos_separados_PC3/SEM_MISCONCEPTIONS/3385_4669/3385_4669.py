medida = input('Medida em A ou H?: ')
var1 = float(input('medida?:'))
if(medida=="A"):
	hectar = var1/2.47105
	print(round(hectar, 2))
else:
	acre = 2.47105*var1
	print(round(acre, 2))