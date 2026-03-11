qf = int(input("digite a quantidade de seguidores de FORSETI: "))
ql = int(input("digite a quantidade de seguidores de LOKI: "))
pf = float(input("Digite o percentual de crescimento dos seguidores de FORSETI: "))
pl = float(input("Digite o percentual de crescimento dos seguidores de loki: "))
anos = 0
habf = qf
habl = ql

while(habl <= habf):
	habf = (habf/100)*pf + habf
	habl = (habl/100)*pl + habl
	anos = anos + 1
print(anos)