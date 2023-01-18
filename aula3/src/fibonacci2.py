def fibonacci(n):
    import pdb; pdb.set_trace()
    first = 0
    second = 1
    if n < 0:
        print("Incorrect input")
         
    elif n == 0:
        return 0

    elif n == 1:
        return second
    else:
        for i in range(1, n):
            third = first + second
            first = second
            second = third
        return second

print(fibonacci(7))