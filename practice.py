num = int(input("Enter the number: "))
while num >=0:
    sum = 0
    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10
    num = sum
print (num)
# pooja fartade