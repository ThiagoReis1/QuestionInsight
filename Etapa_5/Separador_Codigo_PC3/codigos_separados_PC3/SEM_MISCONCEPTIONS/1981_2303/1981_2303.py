coloc = input()
quant = input()

if coloc == "Campeao" and quant =="06-vezes" :
	print("corinthians".upper())
elif coloc == "Campeao" and quant == "03-vezes":
	print("santos".upper())
elif coloc == "Vice-Campeao" and quant == "01-vez":
	print("flamengo".upper())
elif coloc == "Vice-Campeao" and quant == "06-vezes":
	print("internacional".upper())
else:
	print("time de futebol nao identificado".upper())