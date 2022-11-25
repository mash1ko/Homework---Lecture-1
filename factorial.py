n = 0
i = 0
result = 1
n = int(input("Enter number: \n"))

for i in range(0, n):
    i += 1
    result = result *(n-(n-i))
print(result)


