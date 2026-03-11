a = int(input( )) #guerreiros
pt = int(input( )) #pontos de forca do troll
rt = int(input( )) #pontos de forca recuperados do troll
ro = 0 #variavel contadora de rodadas
pf = pt

while(pf>0):
	pf = pf-(a*5)+rt
	ro = ro+1
print(ro)