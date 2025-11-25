# Introduction
# Multi-Agent Platform (Python + AWS Example)

## Components
- Research Agent processor: /agents/research_agent.py
- Memory Agent processor: /agents/memory_agent.py
- Synthesis Agent processor: /agents/synthesis_agent.py
- Orchestration processor: /processor/orchestration.py
- Quality/Monitoring: /processor/quality.py
- DynamoDB Table creation: /cloudEngine/dynamo_setup.py

## Setup
1. Create DynamoDB table using /cloudEngine/dynamo_setup.py
2. Deploy each agent and orchestration as AWS processor functions.
3. Set up API Gateway -> orchestration processor for user requests.
4. Optionally configure OpenSearch + /processor/quality.py for agent monitoring.

## Usage
Send a POST to API Gateway endpoint:
{
  "user_id": "testuser",
  "query": "latest agentic AI frameworks"
}
