import numpy as np
from collections import Counter
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    try:
        # counter dictionary of all items 
        items = Counter(skus)
        prices = [50,30,20,15,40,10,20,10,35,60,70,90,15,40,10,50,30,50,20,20,40,50,20,17,20,21]

        # check item validity
        valid_items = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for item in items.keys():
            if item not in valid_items:
                return -1
        
        ## above could be combined into this if efficiency is required on huge lists + loops optimized
        ## for a smaller list like this I have favoured readability of the code to maintain
        # calculate cost of each item and total
        total = 0 
        tracker = False
        for idx, item in enumerate(valid_items):
            quantity = items[item]
            price = prices[idx]
            # instructions for A
            if item == 'A':
                # implementing cost variations between 3 and 5 products
                cost_var_1_A = quantity%3*price + int(quantity/3)*130
                cost_var_2_A = quantity%5*price + int(quantity/5)*200
                # incase amount bought is a multiple of 8
                if (quantity-5)>=0 and ((quantity-5)-3)>=0:
                    cost_var_3_A = quantity%8*price + int(quantity/5)*200 + int((quantity-5)/3)*130
                    # return min of three options to favour customer
                    cost = min(cost_var_1_A, cost_var_2_A, cost_var_3_A)
                else:
                    # return min of two options to favour customer
                    cost = min(cost_var_1_A, cost_var_2_A)     
            # instructions for B
            elif item == 'B':
                # calculate if any B are free from 2Es
                B_free_quan = int(items["E"]/2)
                quantity -= B_free_quan
                quantity = int(np.maximum(0, quantity))
                cost = quantity%2*price + int(quantity/2)*45
            # instructions for F 
            elif item =='F':
                if quantity>=3:
                    cost = int(quantity/3)*2*price + quantity%3*price
                else: 
                    cost = quantity*price

            # instructions for H 
            elif item == 'H':
                # implementing cost variations between 5 and 10 products
                cost_var_1_H = quantity%5*price + int(quantity/5)*45
                cost_var_2_H = quantity%10*price + int(quantity/10)*80
                # incase amount bought is a multiple of 15
                if (quantity-10)>=0 and ((quantity-10)-5)>=0:
                    cost_var_3_H = quantity%15*price + int(quantity/10)*80 + int((quantity-10)/5)*45
                    # return min of three options to favour customer
                    cost = min(cost_var_1_H, cost_var_2_H, cost_var_3_H)
                else:
                    # return min of two options to favour customer
                    cost = min(cost_var_1_H, cost_var_2_H)     
            # instructions for K 
            elif item == 'K':
                # calculate if any K are free from 2Ks
                cost = quantity%2*price + int(quantity/2)*120 
            # instructions for M 
            elif item == 'M':
                # calculate if any B are free from 2Es
                M_free_quan = int(items["N"]/3)
                quantity -= M_free_quan
                quantity = int(np.maximum(0, quantity))
                cost = quantity*price
            elif item == 'P':
                # calculate if any B are free from 2Es
                cost = quantity%5*price + int(quantity/5)*200                     
            elif item == 'Q':
                # calculate if any B are free from 2Es                    
                Q_free_quan = int(items["R"]/3)
                quantity -= Q_free_quan
                quantity = int(np.maximum(0, quantity))    
                cost = quantity%3*price + int(quantity/3)*80 
            # instructions for U 
            elif item =='U':
                if quantity>=4:
                    cost = int(quantity/4)*3*price + quantity%4*price 
                else: 
                    cost = quantity*price 
            # instructions for V
            elif item == 'V':
                # implementing cost variations between 3 and 5 products
                cost_var_1_V = quantity%2*price + int(quantity/2)*90
                cost_var_2_V = quantity%3*price + int(quantity/3)*130
                # incase amount bought is a multiple of 8
                if (quantity-3)>=0 and ((quantity-3)-2)>=0:
                    cost_var_3_V = quantity%5*price + int(quantity/3)*130 + int((quantity-3)/2)*90
                    # return min of three options to favour customer
                    cost = min(cost_var_1_V, cost_var_2_V, cost_var_3_V)
                else:
                    # return min of two options to favour customer
                    cost = min(cost_var_1_V, cost_var_2_V) 

            # instructions for ['Z', 'S', 'T', 'Y', 'X']
            elif item in ['Z', 'S', 'T', 'Y', 'X']:
                if tracker == True:
                    pass
                else:
                    # process 3 for 45 list in order of highest to lowest priced
                    priority_item_count = [items[item] for item in ['Z', 'S', 'T', 'Y', 'X']]
                    priority_item_prices = [21,20,20,20,17]

                    count = sum(priority_item_count)

                    if count%3 == 0:
                        to_deduct=count
                    else:
                        to_deduct = count-count%3

                    # add cost of all bundles of 3
                    any_three_cost = int(to_deduct/3)*45

                    # iterate through list removing in priority order
                    for ind,val in enumerate(priority_item_count):
                        while (val>0) and (to_deduct>0):
                            val -= 1
                            priority_item_count[ind] -= 1
                            to_deduct -= 1
                            count -= 1

                    # calculate remaining amount
                    product = sum([x*y for x,y in zip(priority_item_prices, priority_item_count)])
                    
                    total += product+any_three_cost
                    # set tracker to true to not process again
                    tracker = True

            # others
            else:
                cost = quantity*price
            total += cost
            cost = 0

        return total

    except:
        raise NotImplementedError()


