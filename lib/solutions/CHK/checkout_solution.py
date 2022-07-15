
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    try:
        # counter dictionary of all items 
        items = Counter(skus)
        prices = [50,30,20,15]

        # check item validity
        valid_items = ['A', 'B', 'C', 'D']
        for item in items.keys():
            if item not in valid_items:
                return -1
        
        ## above could be combined into this if efficiency is required on huge lists + loops optimized
        ## for a smaller list like this I have favoured readability of the code to maintain
        # calculate cost of each item and total
        total = 0 
        for idx, item in enumerate(valid_items):
            quantity = items[item]
            price = prices[idx]
            # instructions for A
            if item == 'A':
                cost = quantity%3*price + int(quantity/3)*130
            # instructions for B
            elif item == 'B':
                cost = quantity%2*price + int(quantity/2)*45
            # others
            else:
                cost = quantity*price
            total += cost

        return total

    except:
        raise NotImplementedError()