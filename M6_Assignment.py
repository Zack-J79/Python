#Start

# Initialize the array with account numbers
account_numbers = [
    8149420, 5333174, 3080098, 6755963, 9526981,
    4449539, 9387197, 5104726, 2931356, 4282637,
    1750219, 6086650, 3164838, 2419590, 4578589,
    9718904, 6749941, 2545408
]

# Sort the array
account_numbers.sort()

# Get the account number from the user
account_number = int(input("Enter an account number: "))

# Search to locate the number in the array
found = False
for num in account_numbers:
    if num == account_number:
        found = True
        break

# Display the result
if found:
    print("The account number is valid.")
else:
    print("The account number is invalid.")

# End
