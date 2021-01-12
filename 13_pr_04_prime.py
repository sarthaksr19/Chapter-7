num = int(input("enter the number\n"))
isPrime = True

for i in range(2, num):
    if (num%i == 0):
        isPrime = False
        break

if isPrime:
    print(num," is a prime number")
else:
    print(num,"is a not prime number")