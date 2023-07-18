import main

balance_account = 0
inventory ={}
history = []

print ("Hello, you are welcome in our warehouse program ")

while True:
   Commands = ["balance",
  "sale",
  "purchase",
  "account",
  "list",
  "warehouse",
  "review",
  "end",
   ]
   print (Commands)
   User_input = input("Please insert a command: ")


   if User_input not in Commands:
      print("wrong input")

   if User_input == 'balance':
      value = int(input("add or subtract money from your account: "))
      balance_account += value
      if balance_account - value < 0:
         print("Wrong input")
      print(balance_account)
      history.append (value)
   
   if User_input == 'sale':
      product_name = input ("Enter a product name: ")
      if product_name not in inventory:
         print ("There are no product in warehouse ")
      if product_name in inventory:
         product_quantity = int(input("Enter product quantity: ")) 
         if inventory [product_name] [0] < (product_quantity):
            print ("Not enough quantity")
         else:
            inventory [product_name] [0] -= product_quantity
            product_price = float(input("Enter product price: "))
            balance_account += product_price * product_quantity
            history.append (product_name)
            history.append (product_quantity)
            history.append (product_price)

   if User_input == 'purchase':
      product_name = input ("Enter a product name: ")
      product_price = float(input("Enter product price: "))
      product_quantity = int(input("Enter product quantity: "))

      if balance_account - product_price * product_quantity < 0:
         print("Wrong input")
      else:
         balance_account == product_price * product_quantity > 0
         balance_account -= product_price * product_quantity
         inventory [product_name] = [product_price, product_quantity]
         history.append (product_name)
         history.append (product_quantity)
         history.append (product_price)

   if User_input == 'account':
      print (balance_account)

   if User_input == 'list':
      print (inventory)
      
   if User_input == 'warehouse':
      product_names = input ("Enter a product name present in your inventory: ")
      if product_names in inventory:
         product = inventory.get(product_names)
         print (product)
      else:
         print ("Product not found")

   if User_input == 'review':
      Complete_history = input("Enter complete for the complete history or range for range history: ")
      if Complete_history == 'complete':
         print (history)
      elif Complete_history == 'range':
         value_from = int(input("Enter the value from start: "))
         value_to = int(input("Enter the value to end: "))
         if len(history) < value_to:
            print("Wrong input")
         print (history[value_from:value_to])

   if User_input == 'end':
      print ("Goodbye")
      main.read_history(history)
      main.read_inventory(inventory)
      main.read_balance(balance_account)
      break