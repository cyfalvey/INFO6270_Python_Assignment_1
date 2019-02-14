# Display all the prime numbers within an interval
upper = int(input("Enter upper range: "))

print("Prime numbers between 0 and",upper,"are:")

for num in range(0,upper + 1):
    # prime numbers are greater than 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)

#Figuring out the product.
x=1
for num in range(0,upper + 1):
    # prime numbers are greater than 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            x*=num
print("and the product of those numbers is:",str(x))
            
#TODO: Figure out how to do the median. Count occurances of non-prime numbers and
#add them to an ordered set. Divide the count by two. If float-int is not 0, there must be an even number of non-prime
#numbers, so add and substract 0.5 to collect both middle numbers and divide the
#sum of those by two.

a=0
for num in range(0,upper + 1):
    # prime numbers are greater than 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                a+=1
                (num % i) #?I think I wrote tis in to add it to a set. Maybe it was always here?
                break

a=float(a)/2.
if a-float(int(a))==0:
    b=int(a)
    c=int(a)
else:
    b=int(a+.5)
    c=int(a-.5)

#Pull item in b slot plus item in c from the set. Divided by 2.

print("and last but not least, the median of the non-prime numbers is:",str((b+c)/2))
