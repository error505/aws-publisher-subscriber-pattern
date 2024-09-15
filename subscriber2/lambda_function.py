import json
import boto3
import os

# Initialize the S3 client
s3_client = boto3.client('s3')
S3_BUCKET_NAME = os.environ['S3_BUCKET_NAME']

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

            # Create a unique filename for the order
            file_name = f"order-{order_id}.json"

            # Upload the order data to S3 as a JSON file
            s3_client.put_object(
                Bucket=S3_BUCKET_NAME,
                Key=file_name,
                Body=json.dumps(message_body)
            )

            print(f"Order {order_id} for customer {customer_name} processed and stored in S3.")

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
