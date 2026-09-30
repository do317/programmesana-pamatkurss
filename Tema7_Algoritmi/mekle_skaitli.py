

import random

x = []
for _ in range(1000):
    x.append(random.randint(1,100))
def linear_search(saraksts, mekletais):
    soli = 0
    for i,elements in enumerate(saraksts):
        soli = soli +1
        if elements==mekletais:
            return i,soli
    return -1, soli

print("A10000 ",linear_search(x,10000))
print("Ax[10] ",linear_search(x,x[10]))


x.sort()
def binary_search(saraksts, mekletais):
    soli = 0
    apaksa = 0 
    augsa = len(saraksts) #šis ir mazliet citādāks, nekā uzdevumā, bet tehniski tas varētu būt ātrāks, jo mazāk == > < pārbaudījumu.
    while apaksa < augsa:
        soli = soli +1
        vidus = (apaksa + augsa) // 2
        v = saraksts[vidus]
        if v<mekletais:
            apaksa = vidus+1
        else:
            augsa = vidus

    return apaksa, soli

print("B10000 ",binary_search(x,10000))
        #x[10] būs līdzīgs x[9], tāpēc are returno 9 dažreiz:
print("Bx[10] ",binary_search(x,x[10]))
print("Bx[0] ",binary_search(x,x[0]))


#20:
#A10000: 20
#Ax[10]: 11
#B10000: 4
#Bx[10]: 4
#Bx[0]: 5

#1000:
#A10000: 1000
#Ax[10]: 11
#B10000: 9
#Bx[10]: 10
#Bx[0]: 10

# binārajai meklēšanai vajag sakārtotu sarakstu, jo tā pēc katra soļa sadala lauku pa divi, un to var tikai darīt, ja visi skaitļi ir sakārtoti.