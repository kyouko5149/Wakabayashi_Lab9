n = int(input("Enter the number of rows: "))
num = 1

for x in range(1, n + 1):
    for y in range(1, x + 1):
        print(num, end=" ")
        num += 1
    print()