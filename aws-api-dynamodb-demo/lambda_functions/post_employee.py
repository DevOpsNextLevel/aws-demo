import boto3
import json
from decimal import Decimal

# Custom serializer for Decimal objects
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj) if obj % 1 == 0 else float(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    try:
        # Initialize DynamoDB
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('EmployeeTable')
        
        # Validate the request body
        if 'body' not in event or not event['body']:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Request body is required'})
            }
        
        # Parse the request body
        body = json.loads(event['body'])
        
        # Validate required fields
        required_fields = ['employee_id', 'name', 'department', 'role', 'salary', 'status', 'join_date']
        for field in required_fields:
            if field not in body:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': f'Missing required field: {field}'})
                }
        
        # Add the new item to DynamoDB
        table.put_item(Item=body)
        
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Employee added successfully'})
        }
    except Exception as e:
        # Log the error
        print(f"Error: {str(e)}")
        
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal server error', 'details': str(e)})
        }
