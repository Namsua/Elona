import pandas as pd
import random
from datetime import date

url = f"https://docs.google.com/spreadsheets/d/{'write your attending google sheet url here'}/gviz/tq?tqx=out:csv&sheet={'VHP'}"
data = pd.read_csv(url)		#VHP andmed

url = f"https://docs.google.com/spreadsheets/d/{'write your individual scores google sheet url here'}/gviz/tq?tqx=out:csv&sheet={'Elona'}"
data2 = pd.read_csv(url)	#Elona andmed

#for i in range (1,len(data2)):
    #print (data2.loc[i][1] + " " + str(int(data2.loc[i][0])))

print ("\n")

kohal = [] #kohalolijate nimed VHP tabelist
for i in range(30):
    if data.loc[0][i] == "30.05.2024": #date.today().strftime("%d.%m.%Y"):
        for y in range (4,len(data)-2):
            if data.loc[y][i] == "1":
                kohal.append(data.loc[y][2])

v = [] #kohalolijate elod
for i in (kohal):
    for y in range(1,len(data2)):
        if data2.iloc[y][1] == i:
            v.append(int(data2.loc[y][0]))

while True: #kaerajaanide lisamiseks ja ülelaskjate eemaldamiseks
    nr = 1
    for i in kohal:
        print (str(nr) + ". " + i + " " + str(v[nr-1]))
        nr+=1
    print ("\n")
    print ("Kas osalejate nimekiri muutus? \n Sisesta y / n")
    k = str(input())
    if k == "n" or k == "":
        break
    print ("Kas keegi jättis tulemata? \n Sisesta mängija nr / n")
    j = input()
    if j != "n":
        j = int(j)
        del(kohal[j-1])
        del(v[j-1])
    print ("Kas keegi tuli juurde? \n Sisesta nimi ja elo tühikuga eraldatult / n")
    j = input()
    if j != "n":
        nimielo = j.split() 
        nimi = nimielo[0]
        elo = nimielo[1]
        kohal.append(nimi)
        v.append(int(elo))

kohal.append(kohal.pop(v.index(max(v)))) #liigutab kõrgeima eloga viimasele kohale et oleks mugavam edaspidi listidega manipuleerida
v.append(v.pop(v.index(max(v))))

print ("\n")

tsükkel = 0
poolelosum = sum(v)//2

while True:
    if tsükkel == 300:
        poolelosum -= 1
        tsükkel = 0
    tsükkel += 1
    poolelo = []
    if len(kohal)%2 == 1:
        poolelo.append(-round(sum(v)/len(kohal)))
        if tsükkel == 299:
            poolelosum += 2
    r=[] #vestid
    while len(r) != len(kohal)//2:
        x = random.randint(0, len(v)-1)
        if r.count(kohal[x]) == 0:
            r.append(kohal[x])
            poolelo.append(v[x])
    if len(kohal)%2 == 0:		#kui meid on paarisarv mängijaid, siis kõige kõrgem ja madalam elo ühes meeskonnas ja kaks kõige kõrgema eloga mängijat pole ühes meeskonnas
        if sum(poolelo) == poolelosum and min(v) in poolelo and max(v) in poolelo:
            vmax = max(v)
            if v.count(max(v)) > 1:	#kui
                if poolelo.count(max(v)) == 1:
                    break
            v.remove (vmax)
            if max (v) not in poolelo: #kontrollib kas 2 tugevaimat on samas meeskonnas
                v.append (vmax)
                break
            v.append (vmax)
    else:		#kui meid on paarituarv, siis kõige madalama eloga mängija pole kunagi meeskonnas, kus on vähem mängijaid ja kõige kõrgema eloga on alati meeskonnas, kus on vähem mängijaid
        if sum(poolelo) == poolelosum and min(v) not in poolelo and max(v) in poolelo:
            break
            
print ("Vestid: ")
for i in r:
    print (i)
    
print ("\n")
print ("Elo kokku: " + str(sum(v)))
print ("Vestide elo: " + str(sum(poolelo)))
