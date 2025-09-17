number = int(input())
if number <= 25:
    for i in range(number, 26):
        print(f"Inside the loop, my variable is {i}")
else:
    print("Error")