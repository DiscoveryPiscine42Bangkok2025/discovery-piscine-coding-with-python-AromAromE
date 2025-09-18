import sys, re
if len(sys.argv) == 3:
    count = re.findall(sys.argv[1], sys.argv[2])
    print(f"{len(count)}\n")