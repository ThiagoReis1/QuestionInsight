taxaestacionamento = 15
taxafixa = 5
ICMS = 20/100

tempbrake = float(input("QUANTAS HORAS SEU VEICULO PERMANECEU NO ESTACIONAMENTO?: "))
taxasservicos = ((tempbrake*taxaestacionamento)+taxafixa)
devepagar = taxasservicos+taxasservicos*(ICMS)

print(round(devepagar,2))