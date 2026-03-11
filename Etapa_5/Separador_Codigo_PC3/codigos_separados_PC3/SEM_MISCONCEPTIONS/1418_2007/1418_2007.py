f_inicial = float(input("forca inicial do lobisomem: "))
lua = int(input("porcentagem visivel da lua: "))
f_final = f_inicial - (23 * (1 - lua/100) )
if (f_final < 0):
	print("ATACO")
else:
	print("CORRO")