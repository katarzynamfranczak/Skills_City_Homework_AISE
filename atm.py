cash_in = 100
card_pin = 1234
sort = 123456
acc_num = 1234567890

print("Welcome to Kat's ATM.")

input_pin = int(input("Enter your pin "))
count = 0
while input_pin != card_pin:
      count += 1
      if count == 3:
            print("You have entered the pin incorrectly 3 times, please contact the bank.")
            break
      print("the pin is incorrect, try again")
      input_pin = int(input("enter your pin "))

while count < 3: 
      print("Choose one option to continue.")
      print("1. Withdraw amount.")
      print("2. Transfer funds.")
      print("3. Check balance")
      print("4. Deposit funds.")
      print("5. Check account information.")
      print("6. Amend information details.")
      print("7. Exit")
      
      menu_selection = int(input("Enter an option that you wish to proceed: "))

# withdraw
      if menu_selection == 1:
            amount = int(input("Enter the amound you wish to withdraw "))
            if amount <= cash_in:
                  cash_in = cash_in - amount
                  print("Your cash is being withdrawn")
            else: 
                  print("It cannot proceed because the amound is higher than avaiable funds.")

    
# transfer
      if menu_selection == 2:
            trans_money = int(input("How much money do you wanna transfer? "))
            if trans_money <= cash_in:
                  cash_in = cash_in - trans_money
                  print("You have transferred ", + trans_money, "now your balance is", + cash_in)
            else: 
                  print("You do not have enough credit, try again with lower amound")

#balance
      if menu_selection == 3:
            decision = input("Do you wish to check your balance?") 
            if decision == "yes":
                  print("You have", + cash_in, "left in your bank account.")


# deposit
      if menu_selection == 4:
            deposit = int(input("What amound you wish to deposit? "))
            if deposit > 0: 
                  print("You have succesfully deposit £", + deposit, "into your account.")
                  cash_in = deposit + cash_in
                  print("You currently have £", + cash_in, "in your bank account.")
            else: 
                  print("Invalid deposit amount. Please enter a number greater than 0.")

#account information
      if menu_selection == 5:
            account_info = input("Do you wish to check your account information? ")

            if account_info == "yes":
                  print("sort code: ", + sort, "account number: ", + acc_num)

#amend information 
      if menu_selection == 6:
            amend_info = input("Do you wish to amend your information? ")

            if amend_info == "yes": 
                  print("You need to contact the bank.") #I tried to write a code to change the info but failed. 
      
      if menu_selection == 7:
            print("Thanks for using Kat's ATM. Have a nice day!")
            break

            





