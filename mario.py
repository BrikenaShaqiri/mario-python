from cs50 import get_int

while True:
    n = get_int("Height: ")
    if n >= 1 and n <= 8:
        break


for i in range(n):
    # Print spaces
    for j in range(n - i - 1):
        print(" ", end="")

    # Print hashes
    for k in range(i + 1):
        print("#", end="")

    # Move to the next line after each row
    print()
