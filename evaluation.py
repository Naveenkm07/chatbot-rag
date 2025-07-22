import os
from arize.pheonix import Client

ARIZE_API_KEY = os.getenv('ARIZE_API_KEY')
ARIZE_SPACE_KEY = os.getenv('ARIZE_SPACE_KEY')

client = None
if ARIZE_API_KEY and ARIZE_SPACE_KEY:
    client = Client(api_key=ARIZE_API_KEY, space_key=ARIZE_SPACE_KEY)

def log_to_arize(user_query, response, context):
    if not client:
        print('[ARIZE NOT CONFIGURED]')
        return
    client.log(
        prompt=user_query,
        response=response,
        context=context
    ) 