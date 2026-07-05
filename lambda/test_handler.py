import json
from handler import lambda_handler

def test_lambda():
    # Create a fake API request
    event = {
        'body': json.dumps({'task': 'Learn AWS Lambda'})
    }
    
    # Call the function
    response = lambda_handler(event, None)
    
    # Check the response
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['task'] == 'Learn AWS Lambda'
    
    print("Test passed successfully!")

test_lambda()
