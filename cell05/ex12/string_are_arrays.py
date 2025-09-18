import sys
if len(sys.argv) == 2:
    count = 0
    for i in sys.argv[1]:
        if i == 'z':
            count += 1
    if count >= 1:
        for _ in range(count):
            print('z', end='')
    else:
        print("none")
else:
    print("none")