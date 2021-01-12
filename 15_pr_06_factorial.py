num = int(input("enter the number\n"))
fact = 1
if(num>=1):
    for i in range(1,num+1):
        fact *= i
        print("factorial of given number is",fact)
    
else:
    print("you entered the wrong number")

