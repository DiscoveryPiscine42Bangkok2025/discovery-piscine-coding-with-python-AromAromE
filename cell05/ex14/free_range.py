import sys
if len(sys.argv) == 3:
    for i in range(int(sys.argv[1]), int(sys.argv[2])+1):
        print(i)
else:
    print("none")