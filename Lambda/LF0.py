import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('lex-runtime')
    user_message = event['messages'][0]['unstructured']['text']
    user_id = 'root'
    lex_bot = 'dining'
    bot_alias = 'TestBotAlias'
    bot_response = client.post_text(
        botName = lex_bot,
        botAlias = bot_alias,
        userId = user_id,
        inputText = user_message
    )

    response = {
        'headers': {
        'Access-Control-Allow-Headers' : 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },

        "messages" : [{
            "type" : "unstructured",
            "unstructured" : {
                "text" : bot_response['message']
            }
        }]
    }
    return response
