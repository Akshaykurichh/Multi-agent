from opensearchpy import OpenSearch

client = OpenSearch(
    hosts = [{'host': 'your-opensearch-endpoint', 'port': 443}],
    http_auth = ('user', 'pass'),
    use_ssl = True
)

def log_quality(agent_name, response):
    client.index(index="agent-quality", body={"agent": agent_name, "response": response})
