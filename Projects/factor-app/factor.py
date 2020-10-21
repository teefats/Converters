def factor():
    running = True
    while running:
        number = int(input("Please enter a number"))
        factors =[]

        for i in range(1, number + 1):        
            if number % i == 0:
                multiples = int(number/i)
                factors.append(multiples)
        print(factors)
        print(f'The factors of {number} are:')
        for elements in factors:
            print(elements)

        print("\nIn summary: ")
        for i in range(int(len(factors) / 2)):
            print(f'{str(factors[i])} * {str(factors[-i-1])} = {str(number)}')
        choice = input('\nRun again (y/n):').lower()
        if choice != 'y':
            running = False
            print("Thank you for using the program. Have a great day")

             
factor()