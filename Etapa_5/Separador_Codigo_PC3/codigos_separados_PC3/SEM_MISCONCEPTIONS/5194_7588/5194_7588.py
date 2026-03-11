missionRate = str(input())
missionReward = float(input())

if(missionRate == 'B'):
	print(str('Classe: ') + str('Chunin'))
	print(round(missionReward * 0.85, 2))
else:
	print(str('Classe: ') + str('Jounin'))
	print(round(missionReward * 0.78, 2))