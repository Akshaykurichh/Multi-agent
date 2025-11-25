import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.create_table(
    TableName='AgentSessions',
    KeySchema=[{'AttributeName': 'UserId', 'KeyType': 'HASH'}],
    AttributeDefinitions=[{'AttributeName': 'UserId', 'AttributeType': 'S'}],
    ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
)
