""" generalization anonymization """
import pandas as pd
from dateutil.parser import parse



"""
Return true if string is a valid date
@param date_string: str, date to check
@param fuzzy: bool, ignore unknown tokens in string
"""
def is_date(date_string, fuzzy=True):
    try: 
        parse(date_string, fuzzy=fuzzy)
        return True
    except ValueError:
        return False



""" generalization anonymization """
def generalize( columns = [], num_range=10, str_level=1, date_type='year' ):
    print('generalize')
    print(columns,num_range,str_level,date_type)
    # columns names list
    col_names = columns.columns.values
    # iterate columns
    for col_name in col_names:
        # store new values
        values = []
        # iterate rows
        for idx, value in enumerate(columns[col_name]):
            print('idx')
            print(idx)
            print('value')
            print(value)
            new_value = None
            # numeric
            if isinstance(value, int) or isinstance(value, float):
                # generate corresponding range
                epochs = value // num_range
                new_value = f'{epochs*num_range} - {(epochs+1)*num_range}'
            # date
            elif is_date(value):
                date = parse(value, fuzzy=True)
                if date_type == 'month':
                    new_value = date.month
                elif date_type == 'year':
                    new_value = date.year
            # string
            elif isinstance(value, str):
                # string levels
                levels = value.split()
                # generalize string
                new_levels = levels
                if len(levels) > str_level:
                    new_levels = levels[ : -str_level]
                new_value = ' '.join(new_levels)
            print('new_value')
            print(new_value)
            # append result
            values.append(new_value)
        # add to dataframe
        columns[col_name] = pd.Series( values )
    # return
    return columns


