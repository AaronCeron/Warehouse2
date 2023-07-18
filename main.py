def read_history(history):
    with open(r'C:\Users\aaron\OneDrive\Desktop\abc\history.txt', 'w') as file:
        file.write (str(history))

def read_inventory(inventory):
    with open (r'C:\Users\aaron\OneDrive\Desktop\abc\inventory.txt', 'w') as file:
        file.write (str(inventory))

def read_balance(balance_account):
    with open (r'C:\Users\aaron\OneDrive\Desktop\abc\balance.txt', 'w') as file:
        file.write (str(balance_account))