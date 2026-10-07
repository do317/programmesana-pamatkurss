rezultati = [90, 45]
print(rezultati)

rezultati[0], rezultati[1] = rezultati[1], rezultati[0]
print(rezultati)

a,b = 1,2
a,b = b,a
#nevajag 3 mainīgos, jo pitons taisa kopiju


import random


rezultati = []

for _ in range(7):
    rezultati.append(random.randint(1,100))

cmps = 0
for j in range(len(rezultati)):
    for i in range(len(rezultati) - 1):
        if(rezultati[i]> rezultati[i + 1]):
            rezultati[i], rezultati[i + 1] = rezultati[i + 1], rezultati[i]
        cmps = cmps +1
    print(rezultati)
    # lielākais ir beigās
print("cmps ",cmps) # sz6: 30, sz7: 42, sz10: 90 sz11: 110
#cmps aug N*(N-1)