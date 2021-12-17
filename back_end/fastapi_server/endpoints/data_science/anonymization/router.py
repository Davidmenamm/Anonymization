''' imports '''
from fastapi import APIRouter, File, Form
from starlette.responses import StreamingResponse
from io import BytesIO
from .anonymize import anonymize
import pandas as pd
import timeit
import json
''' router '''
router = APIRouter(
			prefix="/anonymization",
    		tags=["anonymization"],
			responses={404: {"description": "Not found"}}
			)
''' anonymization main endpoint '''
@router.post("/files", response_class = StreamingResponse)
async def anonymization(file: bytes = File(...), config: str = Form(...)):
	# time init
	tic = timeit.default_timer()
	# file as str
	inMemoryFile = BytesIO(file)
	# dataframe
	df = pd.read_parquet(inMemoryFile)
	config_obj = json.loads(config)
	""" mention that the preprocessing is not done in the application"""
	""" only the anonymization, therefore datasets must come ready"""
	# send to function to handle anonymization
	results_df = anonymize(df, config_obj)
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


