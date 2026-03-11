fgod = int(input("Nº de seguidores de Forseti: "))
lgod = int(input("Nº de seguidores de Loki: "))
ftax = float(input("Crescimento anual de seguidores de Forseti: "))
ltax = float(input("Crescimento anual de seguidores de Loki: "))

f_followers = fgod
l_followers = lgod
anos = 0

while f_followers >= l_followers:
	f_followers = f_followers + (f_followers * ftax / 100)
	l_followers = l_followers + (l_followers * ltax / 100)
	anos = anos + 1
	
print(anos)
	