f0 = float(input("Digite a força inicial do lobisomem: "))
l = float(input("Digite a porcentagem de lua visivel: "))

f = f0-(23*(1-(l/100)))

if(f<0):
	print("ATACO")
else:
	print("CORRO")