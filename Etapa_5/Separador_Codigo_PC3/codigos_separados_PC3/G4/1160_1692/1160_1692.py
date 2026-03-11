h = int(input("Digite a quabtidade de habitantes: "))
v = int(input("Digite a quantidade de vampiros: "))
x = int(input("Digite a quatidade de pessoas mordidas por vampiros: "))
y = int(input("Digite a quantidade de Vampiros mortos por dia: "))

vamp = v
pessoas = h
perx = x * 0.02
pery = y * 0.01
dia = 0

while(vamp >= pessoas):
		vamp = vamp + (vamp * perx)
		pessoas = pessoas + (pessoas * pery)
		dia = dia + 1

print(dia)