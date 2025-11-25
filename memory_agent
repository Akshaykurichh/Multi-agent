import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('AgentSessions')

def lambda_handler(event, context):
    user_id = event['user_id']
    session_ctx = event.get('context')
    if session_ctx:
        table.put_item(Item={'UserId': user_id, 'Context': session_ctx})
    response = table.get_item(Key={'UserId': user_id})
    return {'context': response.get('Item', {}).get('Context', ''), 'agent': 'MemoryAgent'}
