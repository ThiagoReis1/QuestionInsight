tous = input()
qts = int(input())
qa = int(input())

if tous == "T":
	vlr = 4.5*qts
if tous == "S":
	vlr = 5*qts

vlr = vlr + qa * 12

print(vlr)