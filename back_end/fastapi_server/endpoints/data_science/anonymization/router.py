from fastapi import APIRouter, File, Form
from starlette.responses import StreamingResponse
from .anonymize import anonymize
from os import SEEK_SET, SEEK_END
from io import StringIO, BytesIO
import pandas as pd
import feather
import timeit

router = APIRouter(
			prefix="/anonymization",
    		tags=["anonymization"],
			responses={404: {"description": "Not found"}}
			)


@router.post("/files", response_class = StreamingResponse)
async def anonymization(file: bytes = File(...), config: str = Form(...)):
	# time init
	tic = timeit.default_timer()
	# file as str
	inMemoryFile = BytesIO(file)
	# dataframe
	df = pd.read_parquet(inMemoryFile)
	# data types
	# df.astype(

	# )
	# print( df )
	# print( df.info() )
	# df = pd.concat([inputDf]*5000)
	# send to function to handle anonymization
	results_df = anonymize(df, config)
	# print( results_df )
	inMemoryFile.close()
	# output file
	outMemoryFile = BytesIO()
	# feather.write_dataframe(results_df, outMemoryFile, compression='zstd')
	results_df.to_parquet(outMemoryFile, index=True, compression='gzip')
	# response
	response = StreamingResponse(
		iter([outMemoryFile.getvalue()]),
		# media_type='application/octet-stream',
		# media_type='application/zstandard',
		media_type='application/gzip',
		headers={
			'Content-Disposition': 'attachment; filename=dataset.parquet.gzip',
			'Access-Control-Expose-Headers': 'Content-Disposition'
		}
	)
	# print
	# print('server_done')
	outMemoryFile.close()
	# time end
	toc = timeit.default_timer()
	elapsed = toc-tic
	print(f'Time elapsed is aproximately {elapsed} seconds o {elapsed/60} minutes. For n rows {len(df.index)}')  # seconds
	# return
	return response




# @router.post("/files", response_class = StreamingResponse)
# async def anonymization(file: bytes = File(...), config: str = Form(...)):
# 	# file as str
# 	inputFileAsStr = StringIO(str(file,'utf-8'))
# 	# dataframe
# 	df = pd.read_csv(inputFileAsStr)
# 	# send to function to handle anonymization
# 	results_df = anonymize(df, config)
# 	# output file
# 	results_df = pd.concat([results_df]*70000, ignore_index=True)
# 	outFileAsStr = StringIO()
# 	results_df.to_csv(outFileAsStr, index = False)
# 	# response
# 	response = StreamingResponse(
# 		iter([outFileAsStr.getvalue()]),
# 		media_type='text/csv',
#         headers={
#             'Content-Disposition': 'attachment; filename=dataset.csv',
# 			'Access-Control-Expose-Headers': 'Content-Disposition'
#         }
# 	)
# 	# return
# 	return response