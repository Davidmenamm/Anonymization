""" generalization anonymization """
import pandas as pd
from dateutil.parser import parse



"""
Return true if string is a valid date
@param date_string: str, date to check
@param fuzzy: bool, ignore unknown tokens in string
"""
def is_date(date_string, day_first, year_first, fuzzy=True):
    try: 
        parse(date_string, dayfirst=day_first, yearfirst=year_first, fuzzy=fuzzy)
        return True
    except ValueError:
        return False



""" generalization anonymization """
def generalize( columns, num_range=10, str_level=1, date_type='year', day_first=True, year_first=False ):
    print(columns, num_range, str_level, date_type, day_first, year_first)
    print('generalize')
    # columns names list
    col_names = columns.columns.values
    # iterate columns
    for col_name in col_names:
        # store new values
        values = []
        # iterate rows
        for idx, value in enumerate(columns[col_name]):
            new_value = None
            # numeric
            if isinstance(value, int) or isinstance(value, float):
                # generate corresponding range
                epochs = value // num_range
                new_value = f'{epochs*num_range} - {(epochs+1)*num_range}'
            # date
            elif is_date(value, day_first, year_first):
                date = parse(value, fuzzy=True)
                if date_type == 'month':
                    new_value = f'{date.month}'
                elif date_type == 'year':
                    new_value = f'{date.year}'
                elif date_type == 'month-year':
                    new_value = f'{date.month}-{date.year}'
                elif date_type == 'five' or date_type == 'ten':
                    interval = 5 if date_type == 'five' else 10
                    thousands = date.year // 100
                    tenths = date.year % 100
                    epochs = tenths // interval
                    new_value = f'{thousands}{epochs*interval} - {thousands}{(epochs+1)*interval}'
                    new_value = f'{date.year}'
            # string
            elif isinstance(value, str):
                # string levels
                levels = value.split()
                # generalize string
                new_levels = levels
                if len(levels) > str_level:
                    new_levels = levels[ : -str_level]
                new_value = ' '.join(new_levels)
            # append result
            values.append(new_value)
        # add to dataframe
        columns[col_name] = pd.Series( values )
    # return
    return columns


