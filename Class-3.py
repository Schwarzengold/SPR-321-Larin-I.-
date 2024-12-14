def odd(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            yield num

while True:
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        if start > end:
            print("Error: Start > End!")
        else:
            print("Odd numbers in range:", end=" ")
            first = True  
            for odd in odd(start, end):
                if not first:
                    print(", ", end="")
                print(odd, end="")
                first = False
            print()
        print()
        
        cont = input("Do you want to check another range? (y/n): ").strip().lower()
        
        if cont != "y":
            print(" -=<< Goodbye! >>==- ")
            break
    except ValueError:
        print("Error: check your input!")
