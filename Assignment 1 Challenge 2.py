upper = int(input("Enter upper range: "))
# Display all the prime numbers within an interval
print("Prime numbers between 0 and",upper,"are:")
for num in range(0,upper + 1):
    # prime numbers are greater than 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)

#Figuring out the product of prime numbers up to the entered number.
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
            
#Find the median of non-prime numbers.
a=0
nonprimes=set()
for num in range(0,upper + 1):
    # prime numbers are greater than 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                a+=1
                (num % i) #Is this safe to delete? It doesn't seem to be doing anything.
                nonprimes.add(num)
                break

#Don't forget that 1 belongs in this set! (That was a close one.)
nonprimes.add(1)

#Handling the average if there are an even number of non-prime numbers. In retrospect, I realize that I could have counted items in the set. Range. Whatever.
a=float(a)/2.
if a-float(int(a))==0:
    b=int(a)
    c=int(a)
else:
    b=int(a+.5)
    c=int(a-.5)

print("and last but not least, the median of the non-prime numbers is:",str((sorted(nonprimes)[b]+sorted(nonprimes)[c])/2))

print("Whew. Done. This was fun. In fear of forgetting how to do certain things, I haven't slept in days. G'night, Bo!")