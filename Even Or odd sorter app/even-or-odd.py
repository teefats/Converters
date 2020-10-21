def even_or_odd():
    running = True
    while running:
        print("Welcome to the even or odd sorting app")
        numbers = input("Please enter the numbers you want to sort").strip()
        # num_list = list(numbers)
        # nums = num_list.split(",")
        # for num in num_list:
        #     print(int(num))
        type(numbers)
        print(type(numbers))
        letter = numbers.split(",")
        print(letter)
        num_int = []
        for i in range(0, len(letter)):
            letter[i] = int(letter[i])
            num_int.append(letter[i])
        print(num_int)
        print(type(num_int))

        even_num = []
        odd_num = []
        for i in num_int:
            if i % 2 == 0:
                even_num.append(i)
                print(f'{i} is even')
            else:
                print(f'{i} is odd')
                odd_num.append(i)
        print(f'The following {len(even_num)} numbers are even')
        for i in even_num:
            print(i)
        print()
        print(f'The following {len(odd_num)} numbers are even')
        for i in odd_num:
            print(i)
        choice = input("Would you like to run the program (y/n):").lower()
        if choice != 'y':
            print("Thanks for using the app")
            running = False
        


        
        






even_or_odd()