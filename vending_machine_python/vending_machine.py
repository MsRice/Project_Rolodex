snack_db = {
    ## Mints & Gum
    'A1': {
        'name' : 'Juicy Fruit',
        'price' : 1.00,
        'quanity' : 10
    },
    'A2': {
        'name' : 'Mentos',
        'price' : 2.00,
        'quanity' : 10
    },
    'A3': {
        'name' : 'Altoids',
        'price' : 3.00,
        'quanity' : 10
    },
    'A4': {
        'name' : 'Double Bubble',
        'price' : 1.50,
        'quanity' : 10
    },
    'A5': {
        'name' : 'Ice Breakers',
        'price' : 2.50,
        'quanity' : 10
    },
  
  ## Candy
    'B1': {
        'name' : 'Kit-Kat',
        'price' : 3.00,
        'quanity' : 10
    },
    'B2': {
        'name' : 'Snicker',
        'price' : 4.00,
        'quanity' : 10
    },
    'B3': {
        'name' : 'Skittles',
        'price' : 4.00,
        'quanity' : 10
    },
    'B4': {
        'name' : '3 Musketeers',
        'price' : 2.00,
        'quanity' : 10
    },
    'B5': {
        'name' : 'Starburst',
        'price' : 2.00,
        'quanity' : 10
    },
  
  ## Chips
    'C1': {
        'name' : 'Pringles Original',
        'price' : 3.50,
        'quanity' : 10
    },
    'C2': {
        'name' : 'Doritos',
        'price' : 3.50,
        'quanity' : 10
    },
    'C3': {
        'name' : 'Cheetos',
        'price' : 3.50,
        'quanity' : 10
    },
    'C4': {
        'name' : 'Ruffles',
        'price' : 3.50,
        'quanity' : 10
    },
    'C5': {
        'name' : 'Funyuns',
        'price' : 3.50,
        'quanity' : 10
    }
  
}

db_purse = 50
def get_item(item_num):
    return  snack_db[item_num]

def vending(item_num):
    print (item_num['quanity']) 
    # item_num['quanity'] -= 1 
    # print (item_num['quanity']) 
    return item_num['name'] 

        
def amt_validation(price, user_amt):
    if user_amt >= price:
        return True
    else:
        return False

def purchace(price, user_amt):
    global db_purse
    db_purse += price
    change = user_amt - price
    return change

def log(selected_item):
    global db_purse
    print(f' \
          Item purchased : {selected_item} \
            DB Purse : {db_purse}  ')

def idle():
    user_items = input("Ready... ")
    user_items = user_items.split()

    if len(user_items) == 1:
        selected_item  = get_item(user_items[0])
        print(f'{selected_item['name']} .......{selected_item['price']}' )

    elif user_items[1] == 'cash':
        selected_item  = get_item(user_items[0])
        user_amt = float(input("Amount: "))

        isvalid = amt_validation(selected_item['price'] , user_amt)
        
        if isvalid:
            change = purchace(selected_item['price'] , user_amt)
            snack = vending(selected_item)
            print(f'Enjoy your {snack} , despensing change of ${change}')
            log(selected_item)
   
    elif user_items[1] =='credit':
        selected_item  = get_item(user_items[0])
        user_amt = 10.00
        change = purchace(selected_item['price'] , user_amt)
        snack = vending(selected_item)
        print(f'Enjoy your {snack} , refunding credit of ${change}')
        log(selected_item)
    

    
idle()

