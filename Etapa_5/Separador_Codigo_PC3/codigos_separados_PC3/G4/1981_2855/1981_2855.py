c = input("classificacao: ")
n = input("numero de vezes: ")

if((c == "Campeao") and (n == "06-vezes")):
	t = "corinthians".upper()
	print(t)
elif((c == "Campeao") and (n == "03-vezes")):
	t = "santos".upper()
	print(t)
elif((c == "Vice-Campeao") and (n == "01-vez")):
	t = "flamengo".upper()
	print(t)
elif((c == "Vice-Campeao") and (n ==  "06-vezes")):
	t = "internacional".upper()
	print(t)
else:
	print("time de futebol nao identificado".upper())