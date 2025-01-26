import boto3
import json
from decimal import Decimal

# Custom serializer for Decimal objects

class DecimalEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, Decimal):

            # Convert Decimal to float or int based on your use case
            return int(obj) if obj % 1 == 0 else float(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):

    try:
        # Initialize DynamoDB
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('EmployeeTable')

        # Validate query parameters
        if 'queryStringParameters' not in event or 'employee_id' not in event['queryStringParameters']:

            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'employee_id parameter is required'})
            }
        # Get employee_id from query string parameters
        employee_id = event['queryStringParameters']['employee_id']
        # Query the table
        response = table.get_item(Key={'employee_id': employee_id})

        # Check if item exists
        if 'Item' in response:
            return {
                'statusCode': 200,
                'body': json.dumps(response['Item'], cls=DecimalEncoder)
            }
        else:

            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Employee not found'})
            }
    except Exception as e:

        # Log the error (use CloudWatch logs for debugging)
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal server error', 'details': str(e)})
        }
