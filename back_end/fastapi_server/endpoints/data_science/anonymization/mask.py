""" Apply Anonymization Masks to dataset columns"""
import pandas as pd



""" Mask anonymization """
def mask(df, columns, maskNum):
	# apply mask to the desired index
	s = '*'
	n = maskNum
	col = columns[0]
	# fill nulls with empty string
	df.fillna(value = {'text': ''}, inplace=True)
	# vectors
	maskVector = pd.Series(s, index=range(df[col].size) )
	strLengthVector = df[col].str.len()
	notMaskedStrVector = df[col].str[:n*4]
	# print(maskVector, strLengthVector, notMaskedStrVector)
	df[col] = notMaskedStrVector + maskVector * strLengthVector
	# return
	return df
	
# halfStringLengthVector = df[col].str.len() // 2

# result = df.str[:halfStringLengthVector.int]