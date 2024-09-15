import json
import boto3
import os

sns_client = boto3.client('sns')
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']

def lambda_handler(event, context):
    try:
        # Sample order data
        order_data = {
            "orderId": "12345",
            "customerName": "John Doe",
            "items": ["Laptop", "Smartphone", "Headphones"]
        }

        # Publish the message to the SNS topic
        sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=json.dumps(order_data)
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Order published successfully!')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error publishing order: {str(e)}")
        }
