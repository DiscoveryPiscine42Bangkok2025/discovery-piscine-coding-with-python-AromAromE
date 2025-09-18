anum = [2, 8, 9, 48, 8, 22 ,-12, 2]
bnum =anum.copy()
for i in range(len(bnum)):
    bnum[i]+=2
print(f"Original array: {anum}")
print(f"New array: {bnum}")