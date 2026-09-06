from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI(title='ORCA Marine Intelligence API')
app.add_middleware(CORSMiddleware,allow_origins=['*'],allow_methods=['*'],allow_headers=['*'])
@app.get('/api/health')
def health(): return {'status':'ok','service':'ORCA'}
@app.get('/api/ocean-data')
def ocean_data(region='Bay of Bengal'):
    return {'region':region,'mode':'demo-model-telemetry','source_status':'available'}
