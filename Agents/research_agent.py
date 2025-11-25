import requests

def fetch_web_info(query):
    r = requests.get(f"https://api.duckduckgo.com/?q={query}&format=json")
    return r.json()

def lambda_handler(event, context):
    query = event.get('query', '')
    data = fetch_web_info(query)
    return {'data': data, 'agent': 'ResearchAgent'}
