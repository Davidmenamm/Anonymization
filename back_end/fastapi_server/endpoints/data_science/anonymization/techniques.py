""" Handle all types of anonymization """
from .mask import mask
from .noise import noise
from .swap import swap
from .generalize import generalize
import pandas as pd

""" Anonymize function"""
def techniques(df, config):
	# apply pseudonymization
	pseudonym = config['techniques'].pop('pseudonymization', None)[0]
	if pseudonym:
		if 'unique_index' in pseudonym and 'private_columns' in pseudonym:
			print('pseudo')
			df.drop( labels=pseudonym['private_columns'], inplace=True, axis=1 )
			print(df.columns.values)
			print(df)
	# apply anonymization
	for name, configurations in config['techniques'].items():
		for value in configurations:
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
	print(df.columns.values)
	print(df)
	# return
	return df