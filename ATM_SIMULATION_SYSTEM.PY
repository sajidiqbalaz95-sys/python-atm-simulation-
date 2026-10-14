#First of all i make a function name 
def atm_simulation():

    #this function is used to simulate the ATM system
    print("Welcome to the ATM simulation system")

    #write a balance variable to store the balance of the year
    balance = 1000


    #use a while loop to keep the program running until the user choose to exists
    while True:
        print("please choose an option:")
        print("1. Check balance:")
        print("2. Deposit money:")
        print("3. withdraw money:")
        print("4. Exit:")

        #get the user input
        user = int(input("Enter your choice:"))

        
        #use if else statement to check the user input
        if user == 1:
            print("Your balance is:", balance)
        elif user == 2:
            print("Enter the amount to deposit:")
            amount = int(input())
            balance += amount
            print("your new balance is:", balance)
        elif user == 3:
            print("Enter the amount to withdraw:")
            amount = int(input())
            if amount > balance:
                print("Insufficient balance")
            else:
                balance -= amount
                print("your new balance is:", balance)
        elif user == 4:
            print("Thank you for using the ATM simulation system")
            break
atm_simulation()
          




    
