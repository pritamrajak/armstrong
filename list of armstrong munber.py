n=int(input("Enter the limit to list the armstrong number : "))

sum,rem=0,0
print("The list of armstrong number according to your limit are :")
for i in range (1,n+1):
        p=i
        while (i>0):
                rem=i%10
                sum+=rem**3
                i=i//10

        if (sum == p):
                print(p)
                
        rem,sum=0,0
