""" Apply Anonymization Masks to dataset columns"""
import pandas as pd



""" Mask anonymization """
def mask( df_part, direction, mask_num, symbol ):
	# columns names list
	cols = df_part.columns.values
	# iterate columns
	for col in cols:
		# store new values
		values = []
		# iterate rows
		for value in df_part[col]:
			# value length
			val_len = len( str(value) )
			# determine quantity if decimal
			quantity = 0
			if isinstance(mask_num, int):
				quantity = mask_num
			elif isinstance(mask_num, float):
				quantity = int (val_len * mask_num // 1) # floor value
			# difference
			diff = val_len - quantity
			# make value iterable, in case it was not
			val_vect = list( str(value) )
			not_mask_vect = []
			# not masked vector
			if direction == 'right':
				not_mask_vect = val_vect[:diff]
			elif direction == 'left':
				not_mask_vect = val_vect[-diff:]
			# mask vector
			mask_vect = [symbol] * quantity
			# join vectors
			new_value = []
			if direction == 'right':
				new_value = not_mask_vect + mask_vect
			elif direction == 'left':
				new_value = mask_vect + not_mask_vect
			new_val_str = ''.join(new_value)
			# append value
			values.append(new_val_str)
		# substitute new values
		df_part[col] = pd.Series( values )
	df_part['DestCityName']
	# return
	return df_part