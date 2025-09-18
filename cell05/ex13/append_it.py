import sys
ans = []
if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        if i[-3:] == "ism":
            pass
        else:
            ans.append(i+"ism")
    for i in ans:
        print(i)        
else:
    print("none")