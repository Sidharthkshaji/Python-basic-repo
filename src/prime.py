x = int(input("Enter a Number: "))
for i in range(2, x//2):
    if x % i == 0:
        print("Number is Not Prime")
        break
else:print("Number is Prime")
