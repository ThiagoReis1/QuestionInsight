#calculando minha nota porque nao lembro como calcular arctgh na biblioteca math
quetoes=3
nota=10
pontos_por_questao=10/3
questoes_acertadas=int((input("digite quantas voce acertou:  ")))
nota_final=round(questoes_acertadas*pontos_por_questao, 2)
if nota_final<=10:
	print("sua nota eh",nota_final)
else:
	print("mentiroso nem da pra tirar isso")
