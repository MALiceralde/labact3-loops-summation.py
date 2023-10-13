# fixed input is 4

n = int(input("Enter a number: "))

total = 0

for loop1 in range(1, n + 1):
    total += loop1

# Output the result with the formula
print("Formula: 1 + 2 + 3 +", n)
print("Output: ", total)