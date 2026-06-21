valid= False
while not valid: #using nested while loop
    try:
        n=int(input("Enter your age: "))
        #enter age
        while n < 18:

            print("This age is not valid")

        valid= True
    except ValueError:
        print("Invalid") 