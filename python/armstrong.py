num = int(input("Enter a number: "))

def isArmstrong(num):
    sum = 0
    
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if(sum==num):
        return True
    return False

if isArmstrong(num):
    print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")