""" Handle all types of anonymization """
from .mask import mask
import pandas as pd

""" Anonymize function"""
def anonymize(df, config):
	print(type(config))
	print(config)
	# preprocess and etc ..., meanwhile done inside specific files
	# validate in another file ... (especially no overlappingfiles)
	# temporal reset_index
	df.reset_index( drop=True, inplace=True )	
	print('df')
	print(df)
	# apply techniques
	for name, values in config['techniques'].items():
		if name == 'mask':
			direction = values['direction']
			quantity = values['quantity']
			symbol = values['symbol']
			columns = values['columns']
			df_mask = mask(df.loc[:, columns], direction, quantity, symbol)
			for col in columns: df[col] = df_mask[col]
	print( "df['DestCityName']" )
	print( df['DestCityName'] )
	# return
	return df


	

	# params = {}
	# if (config in validMethods):
	# 	method = config
	# 	params['method'] = method
	# 	params['columns'] = ['DestCityName']
	# 	params['config'] = {
	# 		'maskNum' : 3
	# 	}
	# # apply anonymization
	# result_df = None
	# if ( config == 'mask'):
	# 	maskNum = params['config']['maskNum']
	# 	columns = params['columns']
	# 	result_df = mask(df, columns, maskNum)