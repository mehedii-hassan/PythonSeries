# 1+2+3+----+n
n = int(input("Enter a number: "))
sum = 0
for x in range(1, n + 1, 1):
    sum = sum + x
print("Total sum = ", sum)
