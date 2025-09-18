anum = [2, 8, 9, 48, 8, 22 ,-12, 2]
bnum = []
for x in anum:
    if x > 5:
        bnum.append(x + 2) 
print(f"Original array: {anum}")
print(f"New array: {bnum}")