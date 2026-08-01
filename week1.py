def main():
    print("Input n")
    n = int(input())

    if n < 0:
        print("Please enter a positive integer")
        return

    print("Fibonacci sequence:")
    print(0)

    if n == 0:
        return
    
    print(1)

    if n == 1:
        return
    
    a = 0
    b = 1

    for i in range(1, int(n)):
        c = a + b
        print(c)
        a = b
        b = c

if __name__ == "__main__":
    main()