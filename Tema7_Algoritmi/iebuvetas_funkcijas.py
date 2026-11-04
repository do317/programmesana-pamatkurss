
ienaidnieku_hp = [1,2,3,4,5,6,7,8,9,10]

vajakais = min(ienaidnieku_hp)
stiprakais = max(ienaidnieku_hp)

print(f"{vajakais}, {stiprakais}")

for_vajakais = 9999999999
for k,v in enumerate(ienaidnieku_hp):
    if for_vajakais > v:
        for_vajakais = v
print(f"{for_vajakais}, {vajakais}")

import time

x1m = list(range(1000000))
start = time.time()
summa = 0
for k,v in enumerate(x1m):
    summa += v
print(f"for {time.time() - start:.4f}")

start = time.time()
summa_sum = sum(x1m) # ~10x atraka
print(f"sum {time.time() - start:.4f}")
print(f"{summa}, {summa_sum}")
