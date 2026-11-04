apaksa = 1 
augsa = 100

def sk():
    return 73
tries = 0
while True:
    tries +=1
    minejums = (apaksa + augsa) // 2
    print(f"{minejums}")
    if minejums > sk():
        apaksa = minejums + 1
    elif minejums < sk(): augsa = minejums - 1
    else: break
print(f"bin: {tries}")

# ja lineāri: max ir 100 tries