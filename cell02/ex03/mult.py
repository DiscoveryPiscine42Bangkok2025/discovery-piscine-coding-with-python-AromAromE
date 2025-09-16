firstnumber = int(input("Enter the first number: "))
secondnumber = int(input("Enter the second number: "))
result = firstnumber * secondnumber
print(f"{firstnumber} x {secondnumber} = {result}")
if result < 0:
    print("The result is negative")
elif result == 0:
    print("The result is zero")
else:
    print("The result is positive")