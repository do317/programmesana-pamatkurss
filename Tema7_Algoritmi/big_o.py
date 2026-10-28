import time

def iegut_pirmo(dati): return dati[0]



x10 = [1,2,3,4,5,6,7,8,9,0]
x100 = list(range(100))
x1000 = list(range(1000))
x1000000 = list(range(1000000))
sakums = time.time()
iegut_pirmo(x10)
print(sakums, time.time());
sakums = time.time()
iegut_pirmo(x1000000)
print(sakums, time.time());
#1791366479.9263978 1791366479.9264004
#1791366479.9319222 1791366479.9319298
#abi līdzīgi aizņēma laiku


def saskaita(dati):
    sum = 0
    for k,v in pairs(dati):
        sum += k,v
    return sum
def saskaitaSquared(dati):
    sum = 0
    for k,v in pairs(dati):
        sum += saskaita(dati)
    return sum

sakums = time.time()
saskaita(x100)
print(time.time() - sakums);
sakums = time.time()
saskaitaSquared(x100)
print(time.time() - sakums);
sakums = time.time()
saskaita(x1000)
print(time.time() - sakums);
sakums = time.time()
saskaitaSquared(x1000)
print(time.time() - sakums);