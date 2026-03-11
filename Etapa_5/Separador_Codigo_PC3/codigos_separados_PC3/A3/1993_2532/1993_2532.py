aminoacido = input("qual o ami:").lower()
o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.00794
cistidina = (c*3) + (h*7) + n + (o*2) + s
isoleucina = (c*6) + (h*13) + n + (o*2)
metionina = (c*5) + (h*11) + n + (o*2) + s
if (aminoacido == "cisteina"):
	print(round(cisteina, 2))
elif(aminoacido == "isoleucina"):
	print(round(isoleucina, 2))
elif(aminoacido == "metionina"):
	print(round(metionina, 2))
else:
	print("Entrada:", aminoacido)
	print("Dado Invalido")