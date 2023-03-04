successfull = False
for number in range(3):
    print("Attempt")
    if successfull:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

count=0
for i in range(1,10):
    if(i%2==0):
        print(i)
        count=count+1
print("We have", count, "even numbers.")
