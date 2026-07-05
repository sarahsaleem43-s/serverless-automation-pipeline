import json

def lambda_handler(event, context):
    
    # Get data from API request
    body = json.loads(event.get('body', '{}'))
    task = body.get('task', 'No task provided')
    
    # Return response
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'message': 'Task received successfully',
            'task': task
        })
    }
