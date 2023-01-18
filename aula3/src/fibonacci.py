# Function for nth Fibonacci number
def Fibonacci(n):
    import pdb; pdb.set_trace()
    # Check if input is 0 then it will
    # print incorrect input
    print("n =", n)

    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

# o Artur diz 8
#
print(Fibonacci(7))