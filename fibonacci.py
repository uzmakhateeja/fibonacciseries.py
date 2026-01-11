def fibonacci_while(nterms):
    n1, n2 = 0, 1
    count = 0
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence:", n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1, end=", ")
            nth = n1 + n2
            n1, n2 = n2, nth # Update values
            count += 1

fibonacci_while(8) # Prints: 0, 1, 1, 2, 3, 5, 8, 13
