# AWS DynamoDB API Demo

This project demonstrates how to create a REST API using **API Gateway**, **AWS Lambda**, and **DynamoDB** to manage employee data. The API supports two operations:

- **GET**: Fetch employee details by `employee_id`.
- **POST**: Add a new employee to the database.

---

## **Architecture**

1. **API Gateway**: Serves as the entry point for HTTP requests.
2. **Lambda Functions**:
   - GET Lambda: Fetch employee data from DynamoDB.
   - POST Lambda: Add employee data to DynamoDB.
3. **DynamoDB**: A NoSQL database that stores employee data.

---

## **Setup Instructions**

### **Prerequisites**

1. **AWS CLI** installed and configured.
2. **Python 3.x** installed.
3. AWS IAM roles with the following permissions:
   - `dynamodb:GetItem`
   - `dynamodb:PutItem`
   - `lambda:InvokeFunction`
   - `apigateway:POST`

### **Folder Structure**

Organize the demo as follows:

```
aws-dynamodb-api-demo/
├── README.md
├── lambda_functions/
│   ├── get_employee.py
│   └── post_employee.py
├── scripts/
│   ├── create_dynamodb_table.sh
│   ├── deploy_lambda_functions.sh
│   └── create_api_gateway.sh
└── dataset.json
```

---

## **Step-by-Step Setup**

### **1. Create DynamoDB Table**
Run the following script to create a DynamoDB table:

#### Script: `scripts/create_dynamodb_table.sh`
```bash
#!/bin/bash
aws dynamodb create-table \
    --table-name EmployeeTable \
    --attribute-definitions AttributeName=employee_id,AttributeType=S \
    --key-schema AttributeName=employee_id,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST
```

Command to run:
```bash
bash scripts/create_dynamodb_table.sh
```

---

### **2. Create Lambda Functions**

1. **GET Lambda Function**

#### Code: `lambda_functions/get_employee.py`
```python
import boto3
import json
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj) if obj % 1 == 0 else float(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('EmployeeTable')

    if 'queryStringParameters' not in event or 'employee_id' not in event['queryStringParameters']:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'employee_id parameter is required'})
        }

    employee_id = event['queryStringParameters']['employee_id']
    response = table.get_item(Key={'employee_id': employee_id})

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
```

2. **POST Lambda Function**

#### Code: `lambda_functions/post_employee.py`
```python
import boto3
import json

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('EmployeeTable')

    if 'body' not in event or not event['body']:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Request body is required'})
        }

    body = json.loads(event['body'])
    required_fields = ['employee_id', 'name', 'department', 'role', 'salary', 'status', 'join_date']

    for field in required_fields:
        if field not in body:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': f'Missing required field: {field}'})
            }

    table.put_item(Item=body)
    return {
        'statusCode': 201,
        'body': json.dumps({'message': 'Employee added successfully'})
    }
```

---

### **3. Deploy Lambda Functions**

#### Script: `scripts/deploy_lambda_functions.sh`
```bash
#!/bin/bash
zip get_employee.zip lambda_functions/get_employee.py
zip post_employee.zip lambda_functions/post_employee.py

aws lambda create-function \
    --function-name GETEmployee \
    --runtime python3.x \
    --role <LAMBDA_EXECUTION_ROLE_ARN> \
    --handler get_employee.lambda_handler \
    --zip-file fileb://get_employee.zip

aws lambda create-function \
    --function-name POSTEmployee \
    --runtime python3.x \
    --role <LAMBDA_EXECUTION_ROLE_ARN> \
    --handler post_employee.lambda_handler \
    --zip-file fileb://post_employee.zip
```

Run the script:
```bash
bash scripts/deploy_lambda_functions.sh
```
Ensure the lambda role has sufficient permissions to interact with the dynamodb table:
-   AWSLambdaDynamodbExecutionRole
-   AmazonDynamoDBFullAccess
These permissions are overly permissive, consider least privileges in Enterprise environment
---

### **4. Set Up API Gateway**
Run the following script to set up API Gateway and integrate it with Lambda functions:

#### Script: `scripts/create_api_gateway.sh`
```bash
#!/bin/bash
# Create the API Gateway REST API
API_ID=$(aws apigateway create-rest-api --name "EmployeeAPI" --query 'id' --output text)
RESOURCE_ID=$(aws apigateway get-resources --rest-api-id $API_ID --query 'items[0].id' --output text)

# Create /employees resource
EMPLOYEES_ID=$(aws apigateway create-resource \
    --rest-api-id $API_ID \
    --parent-id $RESOURCE_ID \
    --path-part "employees" \
    --query 'id' --output text)

# Add GET and POST methods
aws apigateway put-method \
    --rest-api-id $API_ID \
    --resource-id $EMPLOYEES_ID \
    --http-method GET \
    --authorization-type NONE

aws apigateway put-method \
    --rest-api-id $API_ID \
    --resource-id $EMPLOYEES_ID \
    --http-method POST \
    --authorization-type NONE

# Deploy the API
aws apigateway create-deployment \
    --rest-api-id $API_ID \
    --stage-name dev

echo "API deployed. Invoke URL: https://$API_ID.execute-api.us-east-1.amazonaws.com/dev/employees"
```

Run the script:
```bash
bash scripts/create_api_gateway.sh
```

---

## **Testing**

### **GET Method**
```bash
curl -X GET 'https://<API_ID>.execute-api.us-east-1.amazonaws.com/dev/employees?employee_id=E001'
```

### **POST Method**
```bash
curl -X POST 'https://<API_ID>.execute-api.us-east-1.amazonaws.com/dev/employees' \
-H "Content-Type: application/json" \
-d '{
    "employee_id": "E009",
    "name": "Alice Johnson",
    "department": "Sales",
    "role": "Sales Representative",
    "salary": 75000,
    "status": "Active",
    "join_date": "2023-01-01"
}'
```

---

