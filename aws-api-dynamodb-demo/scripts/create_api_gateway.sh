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