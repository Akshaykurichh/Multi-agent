import json
from agents.memory_agent import MemoryAgent

def lambda_handler(event, context):
    user_id = event['user_id']
    session_data = event.get('context')
    agent = MemoryAgent()
    agent.store_session(user_id, session_data)
    return {
        'statusCode': 200,
        'body': json.dumps({'result': 'Session stored'})
    }
