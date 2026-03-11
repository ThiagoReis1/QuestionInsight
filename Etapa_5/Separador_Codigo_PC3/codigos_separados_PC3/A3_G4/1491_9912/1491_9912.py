F=int(input("Valor do frete: "))

if 0 <= F <= 5000:
	tf = 0.03
	tx = 20
if 5001 < F <= 6000:
	tf = 0.04
	tx = 25
if 6001 < F <= 7000:
	tf = 0.05
	tx = 30
if F > 7000:
	tf = 0.06
	tx = 35
v=F*tf+tx

print(round(v,2))
