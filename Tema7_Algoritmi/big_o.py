import time

def iegut_pirmo(dati): return dati[0]


x10 = [1,2,3,4,5,6,7,8,9,0]
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