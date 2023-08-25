'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  ///
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stuck then read the hint                     ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from decimal import Decimal, getcontext

from collections import namedtuple

# Set the precision for the Decimal calculations
getcontext().prec = 50

tolerance = Decimal('1e-4')

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = 0

    for item in order.items:
        if item.type == 'payment':
            net += Decimal(item.amount)
        elif item.type == 'product':
            net -= Decimal(str(item.amount)) * Decimal(str(item.quantity))
        else:
            return("Invalid item type: %s" % item.type)

    if abs(net) < tolerance:
        net = Decimal(0)

    if net != 0:
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
    else:
        return("Order ID: %s - Full payment received!" % order.id)
