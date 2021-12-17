""" Handle all types of anonymization """
from .mask import mask
from .noise import noise
from .swap import swap
from .generalize import generalize
import pandas as pd

""" Anonymize function"""
def anonymize(df, config):
	print(type(config))
	print(config)
	# preprocess and etc ..., meanwhile done inside specific files
	# validate in another file ... (especially no overlappingfiles)
	# temporal reset_index
	# df.reset_index( drop=True, inplace=True )	
	print('df')
	print(df)
	# apply pseudonymization
	pseudonym = config['techniques'].pop('pseudonym', None)
	if pseudonym:
		if 'unique_index' in pseudonym and 'private_columns' in pseudonym:
			df.drop( labels=pseudonym['columns'], inplace=True )		
	# apply anonymization
	for name, configurations in config['techniques'].items():
		print('configurations')
		print(configurations)
		for value in configurations:
			print('value')
			print(value)
			# columns
			columns = value.pop('columns', None)
			if columns:
				# mask
				if name == 'mask':
					# action
					df_mask = mask(df.loc[:, columns], **value)
					# add results
					for col in columns: df[col] = df_mask[col]
				# noise
				elif name == 'noise':
					# action
					df_noise = noise(df.loc[:, columns], **value)
					# add results
					for col in columns: df[col] = df_noise[col]
				# swap
				elif name == 'swap':
					# action
					df_mask = swap(df.loc[:, columns], **value)
					# add results
					for col in columns: df[col] = df_mask[col]
				# generalize
				elif name == 'generalize':
					# action
					df_mask = generalize(df.loc[:, columns], **value)
					# add results
					for col in columns: df[col] = df_mask[col]
	print(df)
	# return
	return df