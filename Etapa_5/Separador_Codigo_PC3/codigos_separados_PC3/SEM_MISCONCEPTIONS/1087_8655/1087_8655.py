primeira = float(input("primeira nota"))
segunda = float(input("segunda nota"))
terceira = float(input("terceira nota"))
quarta = float(input("quarta nota"))
media = (primeira + segunda + terceira + quarta) / 4

if media >= 7.0:
	  resultado = "Aprovado"
else:
	  resultado ="Reprovado"
	
print(round(media, 2))
print(resultado)

