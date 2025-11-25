def lambda_handler(event, context):
    data = event.get('data')
    context_str = event.get('context')
    summary = f"Synthesized report with context: {context_str}, data: {data}"
    return {'report': summary, 'agent': 'SynthesisAgent'}
