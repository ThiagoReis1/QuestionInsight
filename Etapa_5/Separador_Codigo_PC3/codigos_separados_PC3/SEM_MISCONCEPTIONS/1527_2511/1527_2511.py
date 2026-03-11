#Os deuses de MIdgard

qo_forseti = int(input("Digite a quantidade: "))
qo_loki = int(input("Digite a quantidade: "))
pforseti = float(input("Digite o percentual anual de forseti: "))
ploki = float(input("Digite o percentual anual de loki: "))
anos = 0

while (qo_loki < qo_forseti):
		qo_forseti = qo_forseti + qo_forseti * pforseti/100
		qo_loki = qo_loki + qo_loki * ploki/100
		anos = anos + 1 
print (anos)


		