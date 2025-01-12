'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    if not isinstance(order.items, (list, tuple)):
        return "Invalid order: items must be a list or tuple"

    net = 0

    for item in order.items:
        if not isinstance(item, Item):
            return "Invalid order: all items must be of type Item"
        try:
            amount = float(item.amount)
            quantity = int(item.quantity)
        except ValueError:
            return "Invalid item values in order ID: %s" % order.id

        if item.type == 'payment':
            net += amount
        elif item.type == 'product':
            net -= amount * quantity
        else:
            return "Invalid item type: %s" % item.type

    if net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id
