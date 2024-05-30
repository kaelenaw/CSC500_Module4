class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        self.item_total = float(f'{(self.item_price * self.item_quantity):2f}')
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_total:.2f}")

# Get user input for item1 information
print('Item 1\n')
item1_name = input('Item name: \n')
item1_price = float(input('Item price: \n'))
item1_quantity = int(input('Item quantity: \n'))

# creates item1 from inputs
item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)
item1.print_item_cost()

# Get user input for item2 information
print('\nItem 2\n')
item2_name = input('Item name: \n')
item2_price = float(input('Item price: \n'))
item2_quantity = int(input('Item quantity: \n'))

# creates item2 from inputs
item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)
item2.print_item_cost()

# determines bill total
total = item1.item_total + item2.item_total

# prints out item information and costs as receipt
print('\nTOTAL COST')
print('{n} {q} @ ${p:.2f} = {t:.2f}\n'.format(n = item1_name, p = item1_price, q = item1_quantity, t = item1.item_total))
print('{n} {q} @ ${p:.2f} = {t:.2f}\n'.format(n = item2_name, p = item2_price, q = item2_quantity, t = item2.item_total))
print('Total: ${:.2f}'.format(total))
