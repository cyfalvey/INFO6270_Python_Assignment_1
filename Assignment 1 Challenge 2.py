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
            
#TODO: Figure out how to do the median. Uses the non-printed set before the Else.

MySet([])
for num in range(0,upper + 1):
    # prime numbers are greater than 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                #Add num to MySet
                break

print("and last but not least, the median of the non-prime numbers is:",str())
