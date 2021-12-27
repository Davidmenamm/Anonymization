""" swapping anonymization """


""" swapping anonymization """
def swap( columns, type='independent', seed=0 ):
    # determine type
    if type == 'group':
        columns = columns.sample(   frac=1, random_state=seed, axis=0,
                                    replace=False, ignore_index=True )
    elif type == 'independent':
        # columns names list
        col_names = columns.columns.values
        # iterate columns
        for idx, col_name in enumerate(col_names):
            # sample
            sampled_col = columns[col_name].sample( frac=1, random_state=seed+idx, axis=0,
                                                    replace=False, ignore_index=True )
            # add to dataframe
            columns[col_name] = sampled_col
    # return
    return columns