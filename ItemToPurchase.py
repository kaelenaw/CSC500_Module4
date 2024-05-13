class ItemToPurchase:
    # initializes ItemToPurchase class
    def __init__(self, item_name, item_price, item_quantity):
        item_name = 'none'
        item_price = 0.00
        item_quantity = 0

# Get user input for item1 information
print('Item 1\n')
item1_name = input('Item name: \n')
item1_price = float(input('Item price: \n'))
item1_quantity = int(input('Item quantity: \n'))

# creates item1 from inputs
item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)
item1_total = item1_quantity * item1_price

# Get user input for item2 information
print('\nItem 2\n')
item2_name = input('Item name: \n')
item2_price = float(input('Item price: \n'))
item2_quantity = int(input('Item quantity: \n'))

# creates item2 from inputs
item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)
item2_total = item2_quantity * item2_price

# determines bill total
total = item1_total + item2_total

# prints out item information and costs as receipt
print('\nTOTAL COST')
print('{n} {q} @ ${p} = {t}\n'.format(n = item1_name, p = item1_price, q = item1_quantity, t = item1_total))
print('{n} {q} @ ${p} = {t}\n'.format(n = item2_name, p = item2_price, q = item2_quantity, t = item2_total))
print('Total: ${}'.format(total))
