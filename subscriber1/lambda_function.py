import json
import boto3
import os

# Initialize the DynamoDB client
dynamodb_client = boto3.client('dynamodb')
DYNAMODB_TABLE_NAME = os.environ['DYNAMODB_TABLE_NAME']

def lambda_handler(event, context):
    try:
        # Process each record from the SQS event
        for record in event['Records']:
            message_body = json.loads(record['body'])
            order_id = message_body.get('orderId')
            customer_name = message_body.get('customerName')
            items = message_body.get('items')

            if not order_id or not customer_name or not items:
                raise ValueError('Order ID, Customer Name, or Items are missing in the message.')

            # Store the order data in DynamoDB
            dynamodb_client.put_item(
                TableName=DYNAMODB_TABLE_NAME,
                Item={
                    'orderId': {'S': order_id},
                    'customerName': {'S': customer_name},
                    'items': {'S': json.dumps(items)},
                    'status': {'S': 'Processed'}
                }
            )

            print(f"Order {order_id} for customer {customer_name} processed and stored in DynamoDB.")

        return {
            'statusCode': 200,
            'body': json.dumps('Messages processed successfully.')
        }

    except Exception as e:
        print(f"Error processing messages: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error processing messages: {str(e)}")
        }
