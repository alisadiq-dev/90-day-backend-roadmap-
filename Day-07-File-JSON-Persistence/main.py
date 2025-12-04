from persistent_bank import BankAccount

if __name__ == "__main__":
    # first run -- crate and save 
    account = BankAccount("Ali", 1000)
    account.deposit(500, "salary")
    account.withdraw(200, "shopping")
    account.show_history()
    account.save_to_file() # save to file 
    print("Account saved to file")
    print("\n", "="*10)
    print("\n")

    # second run -- load and show 
    loaded_account = BankAccount.load_from_file()
    loaded_account.show_history()
    print("Account loaded from file")
    print("\n", "="*10)
    print("\n")


    