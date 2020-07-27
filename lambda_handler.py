import json                                                                                                                                                                                                 
import numpy as np

def lambda_handler(event, context):
    arr = np.asarray([1,2,3])
    return {
        'statusCode': 200,
        'body': json.dumps(str(arr))
    }

