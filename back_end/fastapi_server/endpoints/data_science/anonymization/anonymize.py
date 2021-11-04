""" Handle all types of anonymization """
from .mask import mask

""" Anonymize function"""
def anonymize(df, config):
	# valid methods
	validMethods = ['mask', 'generalize']
	# validate config
	params = {}
	if (config in validMethods):
		method = config
		params['method'] = method
		params['columns'] = ['text']
		params['config'] = {
			'maskNum' : 3
		}
	# apply anonymization
	result_df = None
	if ( config == 'mask'):
		maskNum = params['config']['maskNum']
		columns = params['columns']
		result_df = mask(df, columns, maskNum)
	# return
	return result_df