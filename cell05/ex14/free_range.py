import sys
if len(sys.argv) == 3:
    lr = list(range(int(sys.argv[1]), int(sys.argv[2])+1))
    print(lr)
else:
    print("none")