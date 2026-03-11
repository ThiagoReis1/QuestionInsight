ano= int(input())
pais= input().upper()

idade= 2023-ano


if idade>=18 and pais=="B":
	apto= "sim"
	tempoap= 2023-ano-18
	print(apto)
	print(tempoap)
elif idade<18 and pais=="B":
	apto= "nao"
	tempoap= 18-idade
	print(apto)
	print(tempoap)
elif idade>=21 and pais=="R":
	apto= "sim"
	tempoap= 2023-ano-21
	print(apto)
	print(tempoap)
elif idade<21 and pais=="R":
	apto= "nao"
	tempoap= 21-idade
	print(apto)
	print(tempoap)
else:
	apto="invalido"
	print(apto)
