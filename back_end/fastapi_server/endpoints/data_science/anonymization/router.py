''' imports '''
from fastapi import APIRouter, File, Form
from starlette.responses import StreamingResponse
from io import BytesIO
from .techniques import techniques
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
	''' initiate timer '''
	tic = timeit.default_timer()
	
	''' input in-memory file to dataframe'''
	inMemoryFile = BytesIO(file)
	df = pd.read_parquet(inMemoryFile)
	inMemoryFile.close()

	''' json configuration and apply techniques '''
	config_obj = json.loads(config)
	print(config_obj)
	results_df = techniques(df, config_obj)

	''' output in-memory file to streaming response '''
	outMemoryFile = BytesIO()
	results_df.to_parquet(
		outMemoryFile, index=True, compression='gzip')
	response = StreamingResponse(
		iter([outMemoryFile.getvalue()]),
		media_type='application/gzip',
		headers={
		'Content-Disposition': 'attachment; filename=dataset.parquet.gzip',
		'Access-Control-Expose-Headers': 'Content-Disposition'
		}
	)
	outMemoryFile.close()

	''' end timer '''
	elapsed = timeit.default_timer() - tic
	print( f'Time elapsed is aproximately {elapsed/60} minutes.' )

	''' return streaming response'''
	return response