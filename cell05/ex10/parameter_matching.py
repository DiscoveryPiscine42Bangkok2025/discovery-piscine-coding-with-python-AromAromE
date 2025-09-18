import sys

if len(sys.argv) == 2:
    word = input()
    if word == sys.argv[1]:
        print("Good Job")
    else:
        print("Nope, Sorry")
else:
    print("None")