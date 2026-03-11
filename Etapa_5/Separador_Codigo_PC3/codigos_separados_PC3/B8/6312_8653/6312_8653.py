from numpy import *
produto = input().upper()
total = 0
i = 0
bis = 0
cer = 0
lata = 0

while i < len(produto):
	if produto[i] == "B":
		total = total + 3.75
		bis = bis + 1
	elif produto[i] == "C":
		total = total + 7.90
		cer = cer + 1
	elif produto[i] == "E":
		total = total + 9.85
		lata = lata + 1
	i = i + 1
print((round(total, 2)), bis, cer, lata)