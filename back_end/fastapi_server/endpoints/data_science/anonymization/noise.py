""" statistical noise anonymization """
import pandas as pd
import random


""" statistical noise anonymization, for numeric values """
def noise( columns=[], operator='*', quantity=2, rounding=2, rand = False, seed = None ):
    print('noise')
    print(columns,operator,quantity,rounding,rand,seed)
    # columns names list
    col_names = columns.columns.values
    # random seed
    if rand and seed:
        random.seed(seed)
    # iterate columns
    for col_name in col_names:
        # store new values
        values = []
        # iterate rows
        for value in columns[col_name]:
            # cast value
            value = float(value)
            # define quantity
            base = quantity
            if rand:
                base = base * random.random()
            # define operator
            new_value = 0
            if    operator == '+' :  new_value = value + base
            elif  operator == '-' :  new_value = value - base
            elif  operator == '*' :  new_value = value * base
            elif  operator == '/' :  new_value = value / base
            # round result
            new_value_round = round(new_value, rounding)
            if rounding == 0:
                new_value_round = int( new_value_round )
            # append result
            values.append(new_value_round)
        # add to dataframe
        columns[col_name] = pd.Series( values )
    # return
    return columns