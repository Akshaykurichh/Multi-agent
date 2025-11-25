import boto3
import json

def lambda_handler(event, context):
    lambda_client = boto3.client('lambda')

    # Step 1: Research
    r_response = lambda_client.invoke(
        FunctionName='ResearchAgentFunction',
        Payload=json.dumps({'query': event['query']})
    )
    r_payload = json.loads(r_response['Payload'].read().decode())

    # Step 2: Session/Context
    m_response = lambda_client.invoke(
        FunctionName='MemoryAgentFunction',
        Payload=json.dumps({
            'user_id': event['user_id'], 
            'context': f"Research: {event['query']}"
        })
    )
    m_payload = json.loads(m_response['Payload'].read().decode())

    # Step 3: Synthesis
    s_response = lambda_client.invoke(
        FunctionName='SynthesisAgentFunction',
        Payload=json.dumps({
            'data': r_payload['data'],
            'context': m_payload['context']
        })
    )
    s_payload = json.loads(s_response['Payload'].read().decode())

    return {'report': s_payload['report']}
