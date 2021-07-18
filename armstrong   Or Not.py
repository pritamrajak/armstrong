n=int(input("Enter the number to check wether it is a armstrong number or not : "))
p=n
sum,rem=0,0
while (n>0):
        rem=n%10
        sum+=rem**3
        n=n//10

if (sum == p):
        print("The number is armstrong number")
else:
        print("The number is not a armstrong number")
