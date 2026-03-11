ataque = input()
d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())

dano_esp1 = d1 + 6
dano_esp2 = d2 + 6
dano_esp3 = d3 + 6
dano_esp4 = d4 + 6

if(ataque == "espada"):
	dano_esp_total = dano_esp1 + dano_esp2 + dano_esp3 + dano_esp4
	print(dano_esp_total)
else:
	dano_ataque = (d1 + d2 + d3) * d4
	print(dano_ataque)