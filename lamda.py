import json
import os
import mercadopago

def lambda_handler(event, context):
    
    sdk = mercadopago.SDK(os.environ["ACCESS_TOKEN"])
    
    data = {
        "transaction_amount": float(event["transaction_amount"]),
        "token": event["token"],
        "installments": int(event["installments"]),
        "payment_method_id": event["payment_method_id"],
        "payer": {
            "email": event["payer"]["email"],
            "identification": {
                "type": event["payer"]["identification"]["type"],
                "number": event["payer"]["identification"]["number"]
            }
        }
    }

    preference_response = sdk.preference().create(data)
    preference = preference_response["response"]

    return {
        "statusCode": 200,
        'headers' : {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin' : '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            
        },
        "body": json.dumps(
            preference
        ),
    }