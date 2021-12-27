""" Data Masking Anonymization """
import pandas as pd


""" Mask anonymization """
def mask( columns, direction='right', quantity=1, symbol='*' ):
	# columns names list
	col_names = columns.columns.values
	# iterate columns
	for col_name in col_names:
		# store new values
		values = []
		# iterate rows
		for value in columns[col_name]:
			# value length
			val_len = len( str(value) )
			# determine quantity if decimal
			mask_num = 0
			if isinstance(quantity, int):
				mask_num = quantity
			elif isinstance(quantity, float):
				mask_num = int ( round(val_len * quantity, 0) )
			# difference
			diff = val_len - mask_num
			# make value iterable, in case it was not
			val_vect = list( str(value) )
			not_mask_vect = []
			# not masked vector
			if direction == 'right':
				not_mask_vect = val_vect[:diff]
			elif direction == 'left':
				not_mask_vect = val_vect[-diff:]
			# mask vector
			mask_vect = [symbol] * mask_num
			# join vectors
			new_value = []
			if direction == 'right':
				new_value = not_mask_vect + mask_vect
			elif direction == 'left':
				new_value = mask_vect + not_mask_vect
			new_val_str = ''.join(new_value)
			# append value
			values.append(new_val_str)
		# add to dataframe
		columns[col_name] = pd.Series( values )
	# return
	return columns